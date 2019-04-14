import cv2
import numpy
import sys
import os
import csv

src_folder = input()
i=0
totalerror=0
with open("report.csv", "w") as log:
    
    csv_writer = csv.writer(log, quoting=csv.QUOTE_MINIMAL,lineterminator="\n")
    header=("File Name","Amount","Error","Average Error")
    csv_writer.writerow(header)

    for path, dirs, files in os.walk(src_folder):
        
        for each_file in files:
            
            totalseeds = 0
            oldlinecount = 0
            
            file_path = os.path.join(os.path.abspath(path), each_file)
            
            I = cv2.imread(file_path, 0)
            I = cv2.resize(I, (500, 500))
            h,w = I.shape[:2]
            diff = (3,3,3)
            mask = numpy.zeros((h+2,w+2),numpy.uint8)

            cv2.floodFill(I,mask,(0,0), (255,255,255),diff,diff)

            T,I = cv2.threshold(I,180,255,cv2.THRESH_BINARY)
            cv2.imshow('threshold',I)




            I = cv2.medianBlur(I, 5)
            cv2.imshow('blur1',I)

            I = cv2.medianBlur(I, 5)
            cv2.imshow('blur2',I)

            I = cv2.medianBlur(I, 5)
            cv2.imshow('blur3',I)

            I = cv2.medianBlur(I, 5)
            cv2.imshow('blur4',I)
            
            I = cv2.medianBlur(I, 5)
            cv2.imshow('blur4',I)

            I = cv2.medianBlur(I, 5)
            cv2.imshow('blur4',I)

            I = cv2.medianBlur(I, 5)
            cv2.imshow('blur4',I)

            I = cv2.medianBlur(I, 5)
            cv2.imshow('blur4',I)

            I = cv2.medianBlur(I, 5)
            cv2.imshow('blur4',I)

            I = cv2.medianBlur(I, 5)
            cv2.imshow('blur4',I)

            I = cv2.medianBlur(I, 5)
            cv2.imshow('blur4',I)

            I = cv2.medianBlur(I, 5)
            cv2.imshow('blur4',I)

            I = cv2.medianBlur(I, 5)
            cv2.imshow('blur4',I)

            I = cv2.medianBlur(I, 5)
            cv2.imshow('blur4',I)

            I = cv2.medianBlur(I, 5)
            cv2.imshow('blur4',I)



            I = cv2.medianBlur(I, 7)
            cv2.imshow('blur4',I)

            I = cv2.medianBlur(I, 7)
            cv2.imshow('blur4',I)

            I = cv2.medianBlur(I, 7)
            cv2.imshow('blur4',I)

            I = cv2.medianBlur(I, 7)
            cv2.imshow('blur4',I)

            I = cv2.medianBlur(I, 7)
            cv2.imshow('blur4',I)

            I = cv2.medianBlur(I, 7)
            cv2.imshow('blur4',I)

            I = cv2.medianBlur(I, 7)
            cv2.imshow('blur4',I)
            

        
            for y in range(0, h):
                oldc = 0
                linecount = 0
                start = 0   
                for x in range(0, w):
                    c = I[y,x] < 128;
                    if c == 1 and oldc == 0:
                        start = x
                    if c == 0 and oldc == 1 and (x - start) > 10:
                        linecount += 1
                    oldc = c
                if oldlinecount != linecount:
                    if linecount < oldlinecount:
                        totalseeds += oldlinecount - linecount
                    oldlinecount = linecount
                    
            
            filename=each_file.replace(".jpg","")
            realval=int(filename)
            error=realval-totalseeds
            if error < 0:
                error=-error
            else:
                eror=error
            totalerror=totalerror+error
            i=i+1
            avgerror=totalerror/i

            

            if avgerror < 0:
                avgerror=-avgerror
            else:
                avgerror=avgerror
            
            print(file_path,"\t calculated amount is ",totalseeds,"\tactual amount is ",realval,"\terror is", error,"\tavg error is",avgerror)
            
            data=(each_file,totalseeds,error,avgerror)
            csv_writer.writerow(data)
                
            

