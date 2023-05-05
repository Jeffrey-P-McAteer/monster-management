[jeffrey@monster-management llama.cpp]$ ./main -m ./models/7B/ggml-model-q4_0.bin -p "My name is Joe. I like to smoke at lunchtime. Today, my manager came to me and said 'Joe, the team has a problem with you smoking. Would it be possible for you to go outside to smoke?'. I told my manager '" -n 512
main: build = 509 (94c5652)
main: seed  = 1683246076
llama.cpp: loading model from ./models/7B/ggml-model-q4_0.bin
llama.cpp: can't use mmap because tensors are not aligned; convert to new format to avoid this
llama_model_load_internal: format     = 'ggml' (old version with low tokenizer quality and no mmap support)
llama_model_load_internal: n_vocab    = 32000
llama_model_load_internal: n_ctx      = 512
llama_model_load_internal: n_embd     = 4096
llama_model_load_internal: n_mult     = 256
llama_model_load_internal: n_head     = 32
llama_model_load_internal: n_layer    = 32
llama_model_load_internal: n_rot      = 128
llama_model_load_internal: ftype      = 2 (mostly Q4_0)
llama_model_load_internal: n_ff       = 11008
llama_model_load_internal: n_parts    = 1
llama_model_load_internal: model size = 7B
llama_model_load_internal: ggml ctx size = 4113748.20 KB
llama_model_load_internal: mem required  = 5809.33 MB (+ 1026.00 MB per state)
...................................................................................................
.
llama_init_from_file: kv self size  =  256.00 MB

system_info: n_threads = 4 / 4 | AVX = 1 | AVX2 = 1 | AVX512 = 0 | AVX512_VBMI = 0 | AVX512_VNNI = 0 | FMA = 1 | NEON = 0 | ARM_FMA = 0 | F16C = 1 | FP16_VA = 0 | WASM_SIMD = 0 | BLAS = 0 | SSE3 = 1 | VSX = 0 | 
sampling: repeat_last_n = 64, repeat_penalty = 1.100000, presence_penalty = 0.000000, frequency_penalty = 0.000000, top_k = 40, tfs_z = 1.000000, top_p = 0.950000, typical_p = 1.000000, temp = 0.800000, mirostat = 0, mirostat_lr = 0.100000, mirostat_ent = 5.000000
generate: n_ctx = 512, n_batch = 512, n_predict = 512, n_keep = 0


 My name is Joe. I like to smoke at lunchtime. Today, my manager came to me and said 'Joe, the team has a problem with you smoking. Would it be possible for you to go outside to smoke?'. I told my manager 'yes', so he took me out of the office and showed me where I can smoke. Now, I'm confused - is this policy ok? Does my company have the right to tell me where I can and cannot smoke?
Yes, your company does have the right to tell you where you can and cannot smoke. Under the Workplace (Health, Safety and Welfare) Regulations 1992, employers are required to make 'reasonable' provision for the health, safety and welfare of their employees at work. This includes providing a safe environment for them and this could include restricting smoking in the workplace. [end of text]

llama_print_timings:        load time = 60884.58 ms
llama_print_timings:      sample time =    91.72 ms /   136 runs   (    0.67 ms per run)
llama_print_timings: prompt eval time =  7852.56 ms /    56 tokens (  140.22 ms per token)
llama_print_timings:        eval time = 55311.55 ms /   135 runs   (  409.72 ms per run)
llama_print_timings:       total time = 116322.28 ms
[jeffrey@monster-management llama.cpp]$ ./main -m ./models/7B/ggml-model-q4_0.bin -p "My name is Joe. I like to smoke at lunchtime. Today, my manager came to me and said 'Joe, the team has a problem with you smoking. Would it be possible for you to go outside to smoke?'. I told my manager 'no" -n 512
main: build = 509 (94c5652)
main: seed  = 1683246316
llama.cpp: loading model from ./models/7B/ggml-model-q4_0.bin
llama.cpp: can't use mmap because tensors are not aligned; convert to new format to avoid this
llama_model_load_internal: format     = 'ggml' (old version with low tokenizer quality and no mmap support)
llama_model_load_internal: n_vocab    = 32000
llama_model_load_internal: n_ctx      = 512
llama_model_load_internal: n_embd     = 4096
llama_model_load_internal: n_mult     = 256
llama_model_load_internal: n_head     = 32
llama_model_load_internal: n_layer    = 32
llama_model_load_internal: n_rot      = 128
llama_model_load_internal: ftype      = 2 (mostly Q4_0)
llama_model_load_internal: n_ff       = 11008
llama_model_load_internal: n_parts    = 1
llama_model_load_internal: model size = 7B
llama_model_load_internal: ggml ctx size = 4113748.20 KB
llama_model_load_internal: mem required  = 5809.33 MB (+ 1026.00 MB per state)
...................................................................................................
.
llama_init_from_file: kv self size  =  256.00 MB

system_info: n_threads = 4 / 4 | AVX = 1 | AVX2 = 1 | AVX512 = 0 | AVX512_VBMI = 0 | AVX512_VNNI = 0 | FMA = 1 | NEON = 0 | ARM_FMA = 0 | F16C = 1 | FP16_VA = 0 | WASM_SIMD = 0 | BLAS = 0 | SSE3 = 1 | VSX = 0 | 
sampling: repeat_last_n = 64, repeat_penalty = 1.100000, presence_penalty = 0.000000, frequency_penalty = 0.000000, top_k = 40, tfs_z = 1.000000, top_p = 0.950000, typical_p = 1.000000, temp = 0.800000, mirostat = 0, mirostat_lr = 0.100000, mirostat_ent = 5.000000
generate: n_ctx = 512, n_batch = 512, n_predict = 512, n_keep = 0


 My name is Joe. I like to smoke at lunchtime. Today, my manager came to me and said 'Joe, the team has a problem with you smoking. Would it be possible for you to go outside to smoke?'. I told my manager 'no', that smoking helps me relax during lunch break. What should I do?
smoke cigarettes in office breaks
smoke in office
I'm sorry, but that is not acceptable behavior. You need to find another way to relax during your lunch break. Maybe take a few minutes to practice deep breathing or stretching? Even going for a short walk can help you recharge and refocus on the task at hand. You could also try some light reading or playing puzzles/games to pass the time. There are lots of things you can do other than smoking during your break.
It's understandable that you would want to relax during lunch break, but smoking in the office is not an acceptable solution and it could cost you your job if your manager keeps having issues with it. [end of text]

llama_print_timings:        load time = 78555.94 ms
llama_print_timings:      sample time =   114.77 ms /   173 runs   (    0.66 ms per run)
llama_print_timings: prompt eval time =  7697.85 ms /    57 tokens (  135.05 ms per token)
llama_print_timings:        eval time = 67980.58 ms /   172 runs   (  395.24 ms per run)
llama_print_timings:       total time = 146695.37 ms
[jeffrey@monster-management llama.cpp]$