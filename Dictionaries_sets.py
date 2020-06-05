song = {}
song['song_name'] = "Tum hi ho"
song['artist'] = "Arijit Singh"
song["genre"] = "Acoustic music, Filmi, Indian pop"
song['language'] = "Hindi"
song['release_date'] = "16th March"
song['release_year'] = "2013"
song['duration'] = "4.22"
song['writer'] = "Mithoon"
song['movie'] = "Aashiqui 2"
song['label'] = "T-Series"

def guess():
    count = 0
    count1 = 0
    key = input("Enter key: ")
    values = input("Enter value: ")
    for i in song:
        if(key == i):
            if(values == song[i]):
                print(True)
            else:
                print(False)
        if(key!= i):
            count+=1
            if(count>9):
                print(False)
                
for key in song:
    print(key, song[key])

guess()