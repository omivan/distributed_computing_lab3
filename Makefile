all: test program run-python


test: Tests.cpp
	@g++-14 -o test_program Tests.cpp Function.cpp IntegralCalculator.cpp -fopenmp -I/opt/homebrew/opt/libomp/include -L/opt/homebrew/opt/libomp/lib -lomp
	@./test_program

program: main.cpp
	@g++-14 -o program main.cpp Function.cpp IntegralCalculator.cpp -fopenmp -I/opt/homebrew/opt/libomp/include -L/opt/homebrew/opt/libomp/lib -lomp
	@echo "C++ program compiled successfully."

run-python: program
	@python3 main.py
	@echo "Python script executed successfully."

clean:
	@rm -f program
	@echo "Cleaned up the compiled files."

plot: grid_run.py visualise.py
	@python3 grid_run.py
	@python3 visualise.py