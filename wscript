#!/usr/bin/python3
# this is a smith configuration file
# expand and override some targets

DOCDIR = ["documentation", "web"]

APPNAME = "Qishtavah"   
SOURCEFILE = "NotoSansLiving-Regular.ttf"
VERSION = "0.100"
DESC_SHORT = "Autonym font derived from Noto, Qishtavah means 'In its own script' in Hebrew"

font(target = process(APPNAME + '-Regular.ttf', name(APPNAME)), 
    source = create(SOURCEFILE, cmd('hb-info' + ' ${TGT}')),
    fret = fret(params = "-rqm 20"),
    version = VERSION,
    woff = woff(),

    )

def build(ctx) :
        print("\nDowloading fresh langtags.json... ")
        ctx.cmd_and_log("wget -cq https://github.com/silnrsi/langtags/raw/master/pub/langtags.json -O source/langtags.json \n")
        print("\nDowloading fresh Noto Sans Living font... ")
        ctx.cmd_and_log("wget -cq https://github.com/notofonts/notofonts.github.io/raw/main/megamerge/NotoSansLiving-Regular.ttf -O results/NotoSansLiving-Regular.ttf \n")
        print("\nExtracting localnames(s) from langtags... ")
        ctx.cmd_and_log("jq '.[]  | .localname | select ( . )' source/langtags.json | uniq | sort >  source/autonyms.txt \n")
        ctx.cmd_and_log("jq '.[]  | .localnames | select ( . )' source/langtags.json | uniq | sort >>  source/autonyms.txt \n")
        print("\nSubsetting the font... ")
        ctx.cmd_and_log("pyftsubset results/NotoSansLiving-Regular.ttf --layout-features='*' --no-notdef-outline --name-languages='*'  --no-hinting --text-file='source/autonyms.txt' --output-file='results/TempSubset.ttf' \n")
        print("\nRenaming the font filename and internal font name... ")
        ctx.cmd_and_log("ttfname -f 'Qishtavah' results/TempSubset.ttf results/Qishtavah-Regular.ttf \n ")
        print("\nGet stats on the subsetted font... ")
        ctx.cmd_and_log("hb-info results/Qishtavah-Regular.ttf \n") 

def configure(ctx):
        ctx.find_program('jq', var='JQ')
        ctx.find_program('pyftsubset', var='FONTTOOLS')
        ctx.find_program('hb-info', var='HARFBUZZ')

def distclean(ctx) :
        ctx.cmd_and_log(' rm -rf results/ source/* \n')

def clean(ctx) :
        ctx.cmd_and_log(' rm -rf results/ \n')
