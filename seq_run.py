from Scraper.Scraper import Sequence_scraper
import time

if __name__ == "__main__":
    print('start')
    bot = Sequence_scraper()
    bot.land_first_page()
    time.sleep(3)
    bot.accept_cookies()
    time.sleep(2)
    
    bot.get_sequencing()
    time.sleep(3)
    bot.sanger_sequencing()
    time.sleep(3)
    bot.search_equipment()
    bot.sanger_equipments()
    time.sleep(10)
    #bot.quit()