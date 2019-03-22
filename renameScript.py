import os

def main():
    path = input("Enter the path for movie files to rename: ")
    for filename in os.scandir(path):
        if filename.is_dir():
            renameBool = input("Is " + filename.name +
                               " an directory to reorganize/rename? (Y/N):  ")
            if renameBool.lower() == 'y':
                renameDirectory(path + '\\' + filename.name, filename.name)


def renameDirectory(newPath, folderName):
    seasonNum = input("How many episodes are in a season:  ")
    if seasonNum.isdigit():
        currentSeason = 1
        try:
            os.mkdir(newPath+"\\Season " + str(1))
        except OSError as e:
            print("Season folder exists")
        for listedObj in os.scandir(newPath + '\\'):
            if listedObj.is_file():
                filename = listedObj.name
                fname = os.path.splitext(filename)[0]
                extension = os.path.splitext(filename)[1]

                splitFName = fname.split(" - ", 1)

                seriesName = splitFName[0]
                episode = splitFName[1]

                if episode.isdigit():
                    if extension.lower() == ".mkv":
                        proposedSeason = int(int(episode)/int(seasonNum)) + 1
                        if currentSeason != proposedSeason:
                            currentSeason += 1
                            try:
                                os.mkdir(newPath+"\\Season " + str(seasonNum))
                            except OSError as e:
                                print("Failed to create folder:  " + newPath + "\\Season " + str(seasonNum))
                                print(e)
                                
                        if len(seasonNum) < 2:
                            seasonNum = '0' + seasonNum

                        newFName = seriesName + " - S" + str(currentSeason) + "E" + episode + extension
                        print("new Fname: " + newFName)

                        initPath = newPath + '\\' + fname + extension
                        finalPath = newPath + '\\' + "Season " + str(currentSeason) + "\\" + newFName

                        os.rename(initPath, finalPath)


main()

# (Kit ReignFamfrit) write me a program to rename files based on episode list
# (Kit ReignFamfrit) q.q
# (Kit ReignFamfrit) *seriesname* - *episode #*
# (Kit ReignFamfrit) needs to be series - season/episode
# (Kit ReignFamfrit) season # is folder name
