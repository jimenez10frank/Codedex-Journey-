sent_message = 'Hey there! This is a secret message'


with open('sent_message.txt', 'r+') as file:
    file.write(sent_message)

with open('sent_message.txt', 'r+') as file:

    original_message = file.read

    # this moves the cursor to the beginning of the file
    file.seek(0)

    # this is me modifying the message
    unsent_message = "THis message is unsent"

    # this wil truncate the length of the modified message

    file.truncate(len(unsent_message))

    # this wil modifie the message
    file.write(unsent_message)

    # here i display both messages
print("original message:", original_message)
print("unsent message:", unsent_message) 