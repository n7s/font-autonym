Qishtavah font
================

A font that should render all language autonyms.
Qishtavah means 'In its own script' in Hebrew.

An autonym refers to the way a language is called as well as written in its own script by the actual speakers themselves. 

SIL values and helps every language community. A ethos of service to all means no language ignored or left behind. 

An important use case is a inclusive and bandwith-friendly language selector on a website, web app or desktop/mobile app. 

This font is derived from the Noto Sans open font released under the SIL Open Font License.

Proof are provided along with a demo webpage making use of the font. 

Build steps 
============

We are using the smith font development toolchain (https://silnrsi.github.io/silfontdev/).

smith distclean
smith configure
smith build
smith release

It downloads both the upstream Noto Sans Living Regular font file and langtags.json, extracts the autonyms into a text file then subsets the fonts with that information using fonttools. 

Enjoy!

