
# Monster Management


# Research

```bash
contain

# Download https://github.com/mpociot/llamero/releases/tag/v1.0.0
# /j/downloads/Llamero-1.0.0.AppImage

# cd /tmp
# git clone https://github.com/mpociot/llamero.git
# yay -S npm
# npm i
# npm run dev

mkdir -p /mnt/scratch/llama.cpp
git clone https://github.com/ggerganov/llama.cpp.git /mnt/scratch/llama.cpp
cd /mnt/scratch/llama.cpp

make -j
mkdir -p ./models/7B
wget -O ./models/7B/ggml-model-q4_0.bin --continue https://huggingface.co/Pi3141/alpaca-native-7B-ggml/resolve/397e872bf4c83f4c642317a5bf65ce84a105786e/ggml-model-q4_0.bin
./main -m ./models/7B/ggml-model-q4_0.bin -p "A manager often has to fix difficult situations among employees. One such situation is " -n 512


```



