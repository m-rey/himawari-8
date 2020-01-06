const himawari = require('himawari');
const path = require('path');
const fs = require('fs');
const range = require('./utils/range.js');
const Bottleneck = require('bottleneck');
const addMinutes = require('date-fns/addMinutes');
const formatDate = require('date-fns/format');

const limiter = new Bottleneck({
  maxConcurrent: 5,
  minTime: 1000,
});

const ZOOM = 4;
const START_DATE = new Date(2019, 11, 1);
const END_DATE = new Date(2020, 0, 6);

// const BASEPATH = path.join(__dirname, "download")
const BASEPATH = '/Volumes/Time Machine/himawari';

function getNameString(year, month, day, hour, minute) {
  return `${year}-${month
    .toString()
    .padStart(2, '0')}-${day
    .toString()
    .padStart(2, '0')}T${hour
    .toString()
    .padStart(2, '0')}:${minute.toString().padStart(2, '0')}:00`;
}
function getFilepath(nameString) {
  return path.join(
    BASEPATH,
    `${nameString.replace(/\:/g, '-')}_z${ZOOM * 4}.jpg`,
  );
}

async function downloadImage(nameString, filepath) {
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
        console.log(`downloaded ${nameString}`);
        resolve(true);
      },
      error: () => {
        console.log(`error downloading ${nameString}`);
        reject(false);
      },
    });
  });
}

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
    .map(async (d) => {
      return limiter.schedule(() => downloadImage(d.nameString, d.filepath));
    });

  console.log(`downloading ${promises.length} items`);

  const responses = await Promise.all(promises);
  const errorCount =
    responses.filter((d) => d === null || d === false).length || 0;

  if (errorCount) {
    console.log(`Fehler: ${errorCount}`);
  }
})();
