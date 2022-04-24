targets = single_plot.pdf double_plot.pdf scatter.pdf histogram.pdf three_plot.pdf broken_axis.pdf

all: $(targets)

clean: 
	rm $(targets)

single_plot.pdf: single_plot.py
	python single_plot.py

double_plot.pdf: double_plot.py
	python double_plot.py

three_plot.pdf: three_plot.py
	python three_plot.py

scatter.pdf: scatter.py
	python scatter.py

histogram.pdf: histogram.py
	python histogram.py

broken_axis.pdf: broken_axis.py
	python broken_axis.py

