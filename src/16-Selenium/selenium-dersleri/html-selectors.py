import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
file_path = os.path.abspath("kurs.html")
driver.get(file_path)

# find_element()  => tekil

header = driver.find_element(By.ID, "header")
print(f"Header: {header.text}")

sub_title = driver.find_element(By.TAG_NAME, "h2")
print(f"Sub Title: {sub_title.text}")

input_element = driver.find_element(By.NAME, "username")
print(f"Input Placeholder: {input_element.get_attribute('placeholder')}")

course = driver.find_element(By.CLASS_NAME, "course-card")

course_title = course.find_element(By.TAG_NAME, "h2")
course_description = course.find_element(By.TAG_NAME, "p")
course_price = course.find_element(By.TAG_NAME, "span")

print(f"Course Title: {course_title.text}")
print(f"Course Description: {course_description.text}")
print(f"Course Price: {course_price.text}")


# find_elements() => çoğul
courses = driver.find_elements(By.CLASS_NAME, "course-card")
print(f"Number of courses: {len(courses)}")

for kurs in courses:
    title = kurs.find_element(By.TAG_NAME, "h2").text
    description = kurs.find_element(By.TAG_NAME, "p").text
    price = kurs.find_element(By.TAG_NAME, "span").text
    print(f"Course Title: {title}")
    print(f"Course Description: {description}")
    print(f"Course Price: {price}")
    print("-" * 20)


time.sleep(5)

driver.quit()