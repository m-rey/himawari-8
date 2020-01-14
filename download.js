const himawari = require('himawari');
const path = require('path');
const fs = require('fs');
const Bottleneck = require('bottleneck');
const addMinutes = require('date-fns/addMinutes');
const formatDate = require('date-fns/format');

const limiter = new Bottleneck({
  maxConcurrent: 7,
  minTime: 1000,
});

const ZOOM = 4;
const START_DATE = new Date(2019, 11, 1);
const END_DATE = new Date(2020, 0, 9);

// const BASEPATH = path.join(__dirname, 'download');
const BASEPATH = '/Volumes/Time Machine/himawari';

function getFilepath(nameString) {
  return path.join(
    BASEPATH,
    `${nameString.replace(/\:/g, '-')}_z${ZOOM * 4}.jpg`,
  );
}

let stats = {
  total: 0,
  downloaded: 0,
};

function getIndex() {
  stats.downloaded += 1;
  return stats;
}

async function downloadImage({nameString, filepath}) {
  return new Promise(function(resolve, reject) {
    if (fs.existsSync(filepath)) {
      return resolve(true);
    }

    himawari({
      zoom: ZOOM,
      date: nameString,
      outfile: filepath,
      parallel: true,
      //   debug: true,
      success: () => {
        const {total, downloaded} = getIndex();
        console.log(`downloaded ${nameString} (${downloaded}/${total})`);
        resolve(true);
      },
      error: () => {
        const {total, downloaded} = getIndex();
        console.log(`error downloading ${nameString} (${downloaded}/${total})`);
        reject(false);
      },
    });
  });
}

const wrappedDownloadImage = limiter.wrap(downloadImage);

(async () => {
  const tasks = [];
  let currentDate = START_DATE;
  while (currentDate <= END_DATE) {
    const nameString = formatDate(currentDate, "yyyy-MM-dd'T'HH:mm:00");
    const filepath = getFilepath(nameString);
    tasks.push({
      nameString,
      filepath,
    });
    currentDate = addMinutes(currentDate, 10);
  }

  const promises = Array.from(tasks)
    .reverse()
    .filter((d) => {
      return !fs.existsSync(d.filepath);
    })
    .map((d) => {
      return wrappedDownloadImage(d);
    });

  stats.total = promises.length;

  console.log(`downloading ${promises.length} items`);

  let responses = [];
  try {
    responses = await Promise.all(promises);
    console.log('it worked');
  } catch (error) {
    console.log(error);
  }
  const errorCount =
    responses.filter((d) => d === null || d === false).length || 0;

  if (errorCount) {
    console.log(`Fehler: ${errorCount}`);
  }
})();
