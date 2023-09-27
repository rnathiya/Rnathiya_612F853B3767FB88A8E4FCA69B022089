def averageRuns(runs, matches, notout):
 
    out = matches - notout;
 
    if (out == 0):
        return -1;
 
    avg = runs // out;
 
    return avg;
 
runs = 10000;
matches = 260;
notout = 90;
 
avg = averageRuns(runs, matches, notout);
 
if (avg == -1):
    print("NA");
else:
    print(avg);
 