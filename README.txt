Qishtavah font
================

A font that should render all language autonyms.
Qishtavah means 'In its own script' in Hebrew.

An autonym refers to the way a language is called as well as written in its own script by the actual speakers themselves. 

SIL values and helps every language community. A ethos of service to all means no language ignored or left behind. 

An important use case is an inclusive and bandwith-friendly language selector on a website, web app or desktop/mobile app. 

This font is derived from the Noto Sans open font released under the SIL Open Font License.

Proofs are provided along with a demo webpage making use of the font. 

Build steps 
============

We are using the smith open font development toolchain (https://silnrsi.github.io/silfontdev/).

smith distclean
smith configure
smith build
smith sile
smith zip tarball
smith release

It downloads both the upstream Noto Sans Living Regular font file and langtags.json, extracts the autonyms into a text file then subsets the fonts with that information using fonttools. 

Enjoy!


Known issues
=============

Better filtering of duplicates from the langtags.json

Building steps in cmd()s inside of process() rather than build(), which somehow calls the steps in every target...

Currently the subsetting unfortunately looses some important name table metadata, this needs to be fixed. 

