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

  for (var i = 0; i < iterations; i++) {
    console.log("Will execute on: " + interval.next().toString());
  }
} catch (err) {
  console.log('Error: ' + err.message);
}
