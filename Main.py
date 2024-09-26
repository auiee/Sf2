import os
from soundfont import SoundFont

# SoundFontファイルのパス
sf2_file = 'path/to/your/soundfont.sf2'

# SoundFontを読み込む
soundfont = SoundFont(sf2_file)

# 抽出したいサンプルを指定
for preset in soundfont.presets:
    print(f"Preset: {preset.name}")
    
    for sample in preset.samples:
        print(f"  Sample: {sample.name}")
        # サンプルデータの抽出
        sample_data = sample.data
        sample_file_name = f"{preset.name}_{sample.name}.wav"
        
        # サンプルデータをWAVファイルとして保存
        with open(sample_file_name, 'wb') as wav_file:
            wav_file.write(sample_data)

        print(f"  Saved: {sample_file_name}")

print("全サンプルの抽出が完了しました。")
