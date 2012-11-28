# fun with makefiles
# fastlights and testlights
#
setlights: setlights.c lightnames.h lightnames.c layoutloader.h layoutloader.c \
		lightnames.gperf sing.h singtime.c singtime.h
	gcc setlights.c layoutloader.c lightnames.c singtime.c -o setlights -lrt -lyajl -DOLIMEX
	sudo chown root:root setlights
	sudo chmod 6711 setlights
