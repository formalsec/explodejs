Test eval explode :
  $ explode-js exploit test_sink_eval.js
         eval : (`source : __$Str)
  Found 1 problems!
    replaying : test_sink_eval.js...
      running : explode-out/test_sink_eval/test-suite/witness-0.json
       status : true ("success" in stdout)

Test exec explode:
  $ explode-js exploit test_sink_exec.js
         exec : s_concat(["git fetch ", (`remote : __$Str)])
  Found 1 problems!
    replaying : test_sink_exec.js...
      running : explode-out/test_sink_exec/test-suite/witness-0.json
       status : true (created file "success")
Test readFile explode
  $ explode-js exploit test_sink_fs.js
     readFile : (`source : __$Str)
  Found 1 problems!
    replaying : test_sink_fs.js...
      running : explode-out/test_sink_fs/test-suite/witness-0.json
       status : true (undesired file access occurred)

Test polluted explode:
  $ explode-js exploit test_pollution_2.js
        abort : "Prototype pollution detected!"
  Found 1 problems!
    replaying : test_pollution_2.js...
      running : explode-out/test_pollution_2/test-suite/witness-0.json
       status : true ("polluted" in stdout)
  $ explode-js exploit test_pollution_3.js
        abort : "Prototype pollution detected!"
  Found 1 problems!
    replaying : test_pollution_3.js...
      running : explode-out/test_pollution_3/test-suite/witness-0.json
       status : true ("polluted" in stdout)
  $ explode-js exploit test_pollution_4.js
  "Uncaught TypeError"
  "Uncaught TypeError"
  "Uncaught TypeError"
  "Uncaught TypeError"
  "Uncaught TypeError"
  "Uncaught TypeError"
  "Uncaught TypeError"
        abort : "Uncaught Error: I pollute."
  Found 1 problems!
    replaying : test_pollution_4.js...
      running : explode-out/test_pollution_4/test-suite/witness-136.json
       status : true (threw Error("I pollute."))
  unexpected node failure: /home/filipe/projects/explode-js/explode-js/_build/default/test/test_pollution_4.js:52
    throw Error("I pollute.");
    ^
  
  Error: I pollute.
      at Object.<anonymous> (/home/filipe/projects/explode-js/explode-js/_build/default/test/test_pollution_4.js:52:9)
      at Module._compile (node:internal/modules/cjs/loader:1378:14)
      at Module._extensions..js (node:internal/modules/cjs/loader:1437:10)
      at Module.load (node:internal/modules/cjs/loader:1212:32)
      at Module._load (node:internal/modules/cjs/loader:1028:12)
      at Function.executeUserEntryPoint [as runMain] (node:internal/modules/run_main:142:12)
      at node:internal/main/run_main_module:28:49
  
  Node.js v21.6.1

Tests full:
  $ explode-js run test_vfunexported.json
  Genrating explode-out/symbolic_test_0_0.js
         exec : (`x : __$Str)
  Found 1 problems!
    replaying : explode-out/symbolic_test_0_0.js...
  Genrating explode-out/symbolic_test_0_0/literal_0_0.js
      running : explode-out/symbolic_test_0_0/test-suite/witness-0.json
       status : true (created file "success")
  $ explode-js run test_usecase_4.json
  Genrating explode-out/symbolic_test_0_0.js
  "Uncaught TypeError"
  "Uncaught TypeError"
  "Uncaught TypeError"
  "Uncaught TypeError"
  "Uncaught TypeError"
  "Uncaught TypeError"
  "Uncaught TypeError"
        abort : "Uncaught Error: I pollute."
  Found 1 problems!
    replaying : explode-out/symbolic_test_0_0.js...
  Genrating explode-out/symbolic_test_0_0/literal_0_0.js
      running : explode-out/symbolic_test_0_0/test-suite/witness-136.json
       status : true (threw Error("I pollute."))
  Genrating explode-out/symbolic_test_0_0/literal_0_0.js
      running : explode-out/symbolic_test_0_0/test-suite/witness-0.json
       status : false (no side effect)
  unexpected node failure: $TESTCASE_ROOT/explode-out/symbolic_test_0_0.js:51
  if (({}).toString == "polluted") { throw Error("I pollute."); }
                                     ^
  
  Error: I pollute.
      at Object.<anonymous> ($TESTCASE_ROOT/explode-out/symbolic_test_0_0.js:51:42)
      at Module._compile (node:internal/modules/cjs/loader:1378:14)
      at Module._extensions..js (node:internal/modules/cjs/loader:1437:10)
      at Module.load (node:internal/modules/cjs/loader:1212:32)
      at Module._load (node:internal/modules/cjs/loader:1028:12)
      at Function.executeUserEntryPoint [as runMain] (node:internal/modules/run_main:142:12)
      at node:internal/main/run_main_module:28:49
  
  Node.js v21.6.1unexpected node failure: $TESTCASE_ROOT/explode-out/symbolic_test_0_0.js:11
    var segs = path.split('.');
                    ^
  
  TypeError: Cannot read properties of undefined (reading 'split')
      at exports.set ($TESTCASE_ROOT/explode-out/symbolic_test_0_0.js:11:19)
      at Object.<anonymous> ($TESTCASE_ROOT/explode-out/symbolic_test_0_0.js:50:16)
      at Module._compile (node:internal/modules/cjs/loader:1378:14)
      at Module._extensions..js (node:internal/modules/cjs/loader:1437:10)
      at Module.load (node:internal/modules/cjs/loader:1212:32)
      at Module._load (node:internal/modules/cjs/loader:1028:12)
      at Function.executeUserEntryPoint [as runMain] (node:internal/modules/run_main:142:12)
      at node:internal/main/run_main_module:28:49
  
  Node.js v21.6.1
