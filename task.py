from PyPDF2 import PdfFileWriter, PdfFileReader
import glob,os,pikepdf,time
from selenium import webdriver
from pdf2docx import Converter
from RPA.Browser.Selenium import Selenium
import warnings
warnings.filterwarnings('ignore')

browser=Selenium()


pdffiles = []

files_encrypted = []
files_decrypted = []

def file_list():

    for file in glob.glob("*.pdf"):
        pdffiles.append(file)

def file_seg():
    for i in range(len(pdffiles)):
        file = PdfFileReader(pdffiles[i])

        if file.isEncrypted:

            files_encrypted.append(pdffiles[i])
        else:
            files_decrypted.append(pdffiles[i])

def decryptor():
    for i in range(len(files_encrypted)):
        with open("pass.txt", "r") as a_file:
            for line in a_file:
                stripped_line = line.strip()

                try:
                    pdf = pikepdf.open(files_encrypted[i], password=stripped_line)
                    file_name = files_encrypted[i].split(".pdf")
                    pdf.save(file_name[0] + '_decrypted.pdf')
                    pdf.close()
                    os.remove(files_encrypted[i])

                except:
                    pass

def pdf2docx():
    for i in range(len(pdffilesfordocx)):
        pdf_file = pdffilesfordocx[i]

        file_name = pdffilesfordocx[i].split(".pdf")
        word_file = file_name[0] + ".docx"

        cv = Converter(pdf_file)

        cv.convert(word_file, start=0, end=None)
        cv.close()

def pdf2dox():
    for i in range(len(pdffilesdocx)):
        pdf_file=pdffilesdocx[i]

        file_name = pdffilesdocx[i].split(".pdf")
        word_file=file_name[0]+".docx"

        cv= Converter(pdf_file)

        cv.convert(word_file, start=0, end=None)
        cv.close()

def csv_downloader():
    for i in range(len(pdffilesdocx)):
        path_of_pdf=os.path.abspath(pdffilesdocx[i])
        print(path_of_pdf)
        browser.set_download_directory('./')
        browser.open_available_browser('https://www.aconvert.com/pdf/pdf-to-csv/')
        time.sleep(10)
        browser.input_text('xpath://*[@id="file"]',path_of_pdf)
        browser.click_button_when_visible('xpath://input[@id="submitbtn"]')
        time.sleep(20)
        browser.click_element_when_visible('xpath://html/body/div[3]/div[3]/div[2]/div[1]/div[2]/div[1]/div/table/tbody/tr/td[2]/a')
        time.sleep(5)
        browser.close_browser()
        
        csvfiles = []
        for file in glob.glob("*.csv"):
            os.rename(pdffilesdocx[i],file)

            
        


if __name__ == "__main__":
    file_list()
    file_seg()
    decryptor()
    pdffilesdocx = []
    for file in glob.glob("*.pdf"):
        pdffilesdocx.append(file)
    pdf2dox()
    csv_downloader()


