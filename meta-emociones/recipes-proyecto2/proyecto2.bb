LICENSE = "CLOSED"
LIC_FILES_CHKSUM = ""

SRC_URI = "\
	file://emociones.py\
	file://capturador.py\
	file://trainer.py\
	file://logfile.txt\
	file://modeloLBPH.xml\
"

S = "${WORKDIR}"
TARGET_CC_ARCH += "${LDFLAGS}"

do_install(){
	install -d ${D}${bindir}
	install -m 0755 emociones.py ${D}${bindir}
	install -m 0755 capturador.py ${D}${bindir}
	install -m 0755 trainer.py ${D}${bindir}
	install -m 0755 logfile.txt ${D}${bindir}
	install -m 0755 modeloLBPH.xml ${D}${bindir}
}
