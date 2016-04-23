run:
	virtualenv env && source env/bin/activate && \
	pip install mkdocs beautifulsoup4 && \
	sh build.sh $(version)
	-rm -rf env/
clean:
	rm -rf build