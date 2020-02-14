import os


def main():
    """renames all files in the folder according to the pattern: '{collection name} #{number in collection}'"""
    while True:
        print('Enter the full path to the folder with your collection: ', end='')
        folder_full_path = input()
        print('Enter collection name: ', end='')
        new_name = input()

        folder = os.listdir(path=fr'{folder_full_path}')
        folder.sort()

        count = 1
        if len(folder) <= 9:
            n = 1
        elif 9 < len(folder) <= 99:
            n = 2
        else:
            n = 3
        for file in folder:
            old_file = os.path.join(fr'{folder_full_path}', file)
            new_file = os.path.join(fr'{folder_full_path}',
                                    f'{new_name} #{str(count).zfill(n)}'
                                    + os.path.splitext(file)[1]
                                    )
            os.rename(old_file, new_file)
            count += 1

        print('Would you like to continue editing?\nEnter "Yes" or "No":')
        if input() == "No":
            break
