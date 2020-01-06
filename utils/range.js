const range = function(start, stop, step = 1) {
  let numbers = [];
  for (let index = start; index < stop; index += step) {
    numbers.push(index);
  }
  return numbers;
};

module.exports = range;
