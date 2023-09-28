from selene import browser, have, be
import os


def test_registration():
    browser.open('/automation-practice-form')

    # Name
    browser.element('#firstName').type('Vasya')
    browser.element('#lastName').type('Pupkin')
    browser.element('#userEmail').type('Pupkin@example.com')

    # Gender
    browser.element('label[for="gender-radio-1').click()

    # Mobile number
    browser.element('#userNumber').type('1234567890')

    # Date picker
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').type("September")
    browser.element('.react-datepicker__year-select').type("2000")
    browser.element('.react-datepicker__day--001').click()

    # Hobbies
    browser.element('#subjectsInput').type('English').press_enter()
    browser.element('//label[. ="Sports"]').click()

    # Picture
    browser.element('#uploadPicture').send_keys(os.path.abspath('resources/picture.jpg'))

    # Address
    browser.element('#currentAddress').type('123, Street, City, Country')
    browser.element('#react-select-3-input').type('NCR').click().press_enter()
    browser.element('#react-select-4-input').type('Noida').click().press_enter()

    browser.element('#submit').click()

    # Check
    browser.element('.modal-content').should(be.visible)

    browser.element('.table').all('td:nth-of-type(2)').should(
        have.texts(
            'Vasya Pupkin',
            'Pupkin@example.com',
            'Male',
            '1234567890',
            '01 September,2000',
            'English',
            'Sports',
            'picture.jpg',
            '123, Street, City, Country',
            'NCR Noida',
        )
    )
