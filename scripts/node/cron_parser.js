var parser = require('cron-parser');
var util = require('util');

try {
  var args = process.argv;

  if (args.length != 4) {
    console.log(util.format("Usage: node %s '<crontab_expression>' <iterations>\n\nMind the single qoutes!!", args[1]));
    return;
  }

  expression = args[2];
  iterations = args[3];
  interval = parser.parseExpression(expression);
  console.log(util.format("\nUpcoming %s execution dates are:\n"), iterations);
  for (var i = 0; i < iterations; i++) {
    console.log(util.format("%s) %s", i + 1, interval.next().toString()));
  }
} catch (err) {
  console.log('Error: ' + err.message);
}
