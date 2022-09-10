# dice
Do you hate the way that D&DBeyond uses a real-time physics sim to roll their dice? Does your crappy Macbook sound like a VTOL touching down whenever you have to roll with advantage? Don't you wish there was something that would just work quickly and spit out your answer?

## Get started
Well now there is! Simply run `dice.py` and type in your query. For example, if you want to roll an attack with a +11 modifier (with +6 to damage) and preroll damage, you simply have to run `python3 dice.py 1d20 + 11, 1d8 1d4 1d6 + 6`. Alternatively, you can run the script in REPL mode by (now with arrow key roll history!) and run your queries until you kill the program or type `exit`.

### `dice.py` with arguments
```
python3 dice.py <query>
```

Running `dice.py` with command-line arguments evaluates `query` and prints the result, roll-by-roll.

### `dice.py` in REPL mode
```
python3 dice.py
```

Running `dice.py` without command-line arguments enters REPL (read evaluate print loop) mode. In this mode, you can type a query into the console and hit ENTER, then your query will be evaluated. Tip: use the UP and DOWN arrows to navigate through your query history.


## Language
### Dice
When we talk about dice, we're referring to a quantity (typically 1) and a number of sides. For example, `5d6` is taking five standard dice, rolling them, and summing the results.

### Roll
A roll is a set of dice and a modifier. For example, `2d6 1d4 + 13`. When evaluated, we evaluate each of the dice, summing the results, then adding the modifier.

### Query
A query is a single line of input to the program, made up one or more rolls separated by a delimiter (either `;`, `:`, or `,`). Queries are useful for prerolling results of attacks so your party isn't waiting on you while D&DBeyond figures out how a d4 behaves when it tumbles atop a sea of d6's. For example, `1d20 + 11; 1d8 4d6 + 12` is a query that evaluates the rolls `1d20 + 11` and `1d8 4d6 + 12`. EZPZ.

