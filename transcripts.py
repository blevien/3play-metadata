import requests
import unicodecsv
import datetime
from settings import api_key

def getTranscripts():
    current_page = 1
    total_pages = 1

    #handle paginated API response
    while current_page <= total_pages:

        response = requests.get('http://api.3playmedia.com/files?apikey=' + api_key + '&per_page=200&page=' + str(current_page))
        data = response.json()
        total_pages = data['summary']['total_pages']
        print response, current_page, total_pages
        #print json.dumps(response.json(), sort_keys=True, indent=4, separators=(',', ': '))

        toCSV = data["files"]
        keys = ["attribute1",
                "attribute2",
                "attribute3",
                "batch_id",
                "batch_name",
                "callback_url",
                "created_at",
                "deadline",
                "description",
                "downloaded",
                "duration",
                "id",
                "language_id",
                "name",
                "project_id",
                "rush",
                "state",
                "thumbnail_url",
                "turnaround_level_id",
                "updated_at",
                "video_id",
                "word_count"]

        f = open(str(datetime.datetime.now().date()) + '.csv', 'a')
        dict_writer = unicodecsv.DictWriter(f, keys)
        if current_page < 2:
            dict_writer.writer.writerow(keys)
        dict_writer.writerows(toCSV)

        current_page = data['summary']['current_page'] +1

if __name__ == "__main__":
    getTranscripts()


exit()