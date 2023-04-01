import numpy as np

def random_predict(number:int=1) -> int:

    count = 0
    
    min_number = 1
    
    max_number = 100
    
    while True:
        
        count+=1
        
        predict_number=np.random.randint(1, 60) # предполагаемое число
        if predict_number < number:
            min_number = predict_number + 1
            predict_number=np.random.randint(min_number, max_number)
            
        if predict_number > number:
            max_number = predict_number + 1
            predict_number=np.random.randint(min_number, max_number)
            
        if number == predict_number:
            min_number = 1
            max_number = 100
            break # выход из цикла если угадали
        
    return(count)

def score_game(random_predict) -> int:

    count_ls = []
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
        score = int(np.mean(count_ls))
        print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
        return(score)


if __name__=='__main__':
    # RUN
    score_game(random_predict)


