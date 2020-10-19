git:
	git add .
	git commit -m "$m"
	git push -u origin HEAD:master


freeze:
    pip freeze | grep -v "pkg-resources" > requirements.txt


free8:
	sudo fuser -k 8000/tcp
	
free5:
	sudo fuser -k 5000/tcp
 