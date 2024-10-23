import subprocess
import csv


intervals_list = [100 * 10**i for i in range(7)]

threads_list = [1, 2, 4, 8, 16, 32]


csv_file = 'execution_times.csv'


headers = ['Кількість інтервалів'] + [f'Час {threads} потоків (сек.)' for threads in threads_list]

with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)

    
    for intervals in intervals_list:
        
        execution_times = [intervals]

    
        for threads in threads_list:
           
            result = subprocess.run(["./program", str(intervals), str(threads)], capture_output=True, text=True)

          
            if result.returncode == 0:
                output = result.stdout.splitlines()
              
                execution_time_str = output[1].replace('Час виконання:', '').replace('секунд', '').strip()
                try:
                    execution_time = float(execution_time_str) 
                    execution_times.append(execution_time)  
                except ValueError:
                    print(f"Неможливо перетворити час виконання на float: {execution_time_str}")
                    execution_times.append(None)
            else:
                print(f"Помилка виконання для {intervals} інтервалів і {threads} потоків")
                execution_times.append(None)

        writer.writerow(execution_times)

print(f"Час виконання збережено в {csv_file}")
