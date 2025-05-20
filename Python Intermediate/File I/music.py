liked_songs = {
    'ot7style': 'leaf ward',
    'got back': 'carti',
    'amapiano': 'coffee',
}

def write_liked_songs_to_file(liked_songs, file_name):
    with open(file_name, 'w') as file:
        file.write("liked songs:\n")
        for song, artist in liked_songs.items():
            file.write(f"{song} by {artist}\n")
        print(f"succescfully added liked songs to {file_name}")    

write_liked_songs_to_file(liked_songs, "liked_songs.txt")