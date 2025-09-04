from scraper import Scraper

if __name__ == '__main__':
    scraper = Scraper()
    scraper.OpenPage('https://www.moodle.aau.dk/course/view.php?id=56718')

    input("Press Enter when logged in...")

    lecture_count = 2
    scan_lectures = True
    while scan_lectures:
        lecture_text = scraper.GetText(f"/html/body/div[2]/div[4]/div/div/div[5]/section/div/div/div[2]/div/div/ul/li[{lecture_count}]/div[2]/div/div/div/div") 
        print("\n\n")
        print(lecture_count)
        print(lecture_text)
        lecture_count += 1

    input()