LICENSE = "CLOSED"
LIC_FILES_CHKSUM = ""

SRC_URI = "\
	file://recmov.py\
	file://info.py\
	file://recmov2.py\
	file://video.mp4\
	file://image.jpg\
	file://test.py\
"

S = "${WORKDIR}"
TARGET_CC_ARCH += "${LDFLAGS}"

do_install(){
	install -d ${D}${bindir}
	install -m 0755 recmov.py ${D}${bindir}
	install -m 0755 recmov2.py ${D}${bindir}
	install -m 0755 info.py ${D}${bindir}
	install -m 0755 video.mp4 ${D}${bindir}
	install -m 0755 image.jpg ${D}${bindir}
	install -m 0755 test.py ${D}${bindir}
}
