import requests

page = 1

url = 'https://www.udemy.com/api-2.0/search-courses/?p={page}&q=python&src=ukw&skip_price=true'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0',
    'Referer': 'https://www.udemy.com/courses/search/?p={page}&q=python&src=ukw'
}
response = requests.get(url=url, headers=headers).json()
# print(response['courses'])

# url, rating

total = 0
for course in response['courses']:
    rating = course['rating']

    if rating > 4.0:
        course_info = {
            'url': 'https://www.udemy.com' + course['url'],
            'rating': course['rating']
        }
        print(course_info)
    total += 1
print("Total no. of websites: "+str(total))
