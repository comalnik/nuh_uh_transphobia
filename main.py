from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions 
from selenium_recaptcha_solver import RecaptchaSolver
import time
import random
import os
import csv


score = 0
while True:
    #get fake details
    lines = 3000
    random_line_num = random.randint(1, lines - 1)
    with open("fake-details/FakeNameGenerator.com.csv") as fakes:
        reader = csv.reader(fakes)
        for i, row in enumerate(reader):
            if i == random_line_num:
                x = row


    name_detail = str(x[0] + " " + x[1])
    address_detail = str(x[2])
    email_detail = str(x[3])
    phone_detail = str(x[4]).replace("-", " ")
    useragent = str(x[5])


    with open("fake_fields/entities.txt", "r") as file:
        random_entity = random.choice(file.readlines())

    with open("fake_fields/who.txt", "r") as file:
        who = random.choice(file.readlines())

    with open("fake_fields/information.txt", "r") as file:
        information = random.choice(file.readlines())

    with open("fake_fields/resolve.txt", "r") as file:
        resolve = random.choice(file.readlines())

    with open("fake_fields/how.txt", "r") as file:
        how = random.choice(file.readlines())

    with open("fake_fields/evidence.txt", "r") as file:
        evidence = random.choice(file.readlines())


    
    options = Options()
    #options.add_experimental_option("detach", True)

    #random useragent(from fake details csv)
    options.add_argument("user-agent=" + useragent)

    #start webdriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("https://ut-sao-special-prod.web.app/sex_basis_complaint2.html")
    driver.maximize_window()
    solver = RecaptchaSolver(driver=driver)





    #couldnt figure out selenium explicit waits
    def load_check():
        try:
            time.sleep(1)
            dropdown = driver.find_element(By.XPATH, '//*[@id="form-row"]/form/div[1]/button').click();
        except:
            return(load_check())

    load_check()

    #input entity
    entity_input = driver.find_element(By.XPATH, '//*[@id="form-row"]/form/div[1]/div/div[1]/input');
    entity_input.send_keys(random_entity)

    #checkboxes
    random_num1 = random.randint(1,9)
    checkbox_input = driver.find_element(By.ID, 'cb' + str(random_num1));
    action = ActionChains(driver)
    action.move_to_element(checkbox_input).perform()
    action.click(checkbox_input).perform()

    #writing fields
    who_field = driver.find_element(By.XPATH, '//*[@id="cd_q1"]/div[1]');
    who_field.send_keys(who)

    information_field = driver.find_element(By.XPATH, '//*[@id="cd_q2"]/div[1]');
    information_field.send_keys(information)

    resolve_field = driver.find_element(By.XPATH, '//*[@id="cd_q3"]/div[1]');
    resolve_field.send_keys(resolve)

    how_field = driver.find_element(By.XPATH, '//*[@id="cd_q4"]/div[1]');
    how_field.send_keys(how)

    evidence_field = driver.find_element(By.XPATH, '//*[@id="cd_q5"]/div[1]');
    evidence_field.send_keys(evidence)

    #anonymity checkboxes
    random_num2 = random.randint(1,3)
    if random_num2 == 1:
        random_anon = "00N1K00000fXXXy"
    elif random_num2 == 2:
        random_anon = "00N1K00000fHhXz"
    elif random_num2 == 3:
        random_anon = "00N1K00000fXXY0"

    anonymity_input = driver.find_element(By.ID, random_anon);
    action.move_to_element(anonymity_input).perform()
    action.click(anonymity_input).perform()


    #fake details input
    name = driver.find_element(By.XPATH, '//*[@id="00N1K00000fX1ND"]');
    name.send_keys(name_detail)

    address = driver.find_element(By.XPATH, '//*[@id="00N1K00000fXXY3"]');
    address.send_keys(address_detail)

    email = driver.find_element(By.XPATH, '//*[@id="00N1K00000fWywZ"]');
    email.send_keys(email_detail)

    phone = driver.find_element(By.XPATH, '//*[@id="00N1K00000fWywe"]');
    phone.send_keys(phone_detail)



    #acknowledgement checkboxes
    ack1 = driver.find_element(By.ID, "check_certify");
    action.move_to_element(ack1).perform()
    action.click(ack1).perform()

    ack2 = driver.find_element(By.ID, "check_certify_2");
    action.move_to_element(ack2).perform()
    action.click(ack2).perform()

    #solve captcha
    recaptcha_iframe = driver.find_element(By.XPATH, '//*[@id="form-row"]/form/div[30]/div/div/iframe')
    action.move_to_element(recaptcha_iframe).perform()
    solver.click_recaptcha_v2(iframe=recaptcha_iframe)
    
    #submit
    submit = driver.find_element(By.ID, "btn-submit-complaint2");
    action.move_to_element(submit).perform()
    action.click(submit).perform()

    
    time.sleep(2)
    score = score + 1
    print(score)
    driver.close()

# :3
