import pandas as pd

def read_csv(filename):
    df = pd.read_csv(filename)
    return df

def write_csv(data, File):
    data.to_csv(File.replace('.csv','sorted.csv'), encoding='utf-8')
    
def Sort_By(df, F):
    headers = list(df)
    df = df.set_index(get_idx(headers))
    print(df)
    write_csv(df, F)
    
    
def get_idx(h):
    Q = 'Select the field you would like to sort the data by:\n'
    for i in h:
        Q = Q + str(h.index(i)+1) + ":" + i +"\n"
    sorter = int(input(Q))
    while not 0<sorter<=len(h):
        print("Invalid Input")
        sorter = int(input(Q))
    return h[sorter-1]
    
        
if __name__ == '__main__':
    file = "../sample/Test.csv"
    Sort_By(read_csv(file), file)
