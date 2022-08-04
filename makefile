PREFIX = /usr/local

acf: acf.sh acf.awk acf.tsv
	cat acf.sh > $@
	echo 'exit 0' >> $@
	echo '#EOF' >> $@
	tar czf - acf.awk acf.tsv >> $@
	chmod +x $@

test: acf.sh
	shellcheck -s sh acf.sh

clean:
	rm -f acf

install: acf
	mkdir -p $(DESTDIR)$(PREFIX)/bin
	cp -f acf $(DESTDIR)$(PREFIX)/bin
	chmod 755 $(DESTDIR)$(PREFIX)/bin/acf

uninstall:
	rm -f $(DESTDIR)$(PREFIX)/bin/acf

.PHONY: test clean install uninstall
