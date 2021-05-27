PRE-list
========

List of (automatic) protocol reverse engineering tools/methods/approaches for network protocols<br/>

This is a collection of 69 scientific papers about (automatic) protocol reverse engineering (PRE) methods and tools. The papers are categorized into different groups so that it is more easy to get an overview of existing solutions based on the problem you want to tackle.<br/>

The collection is based on the following three surveys and got extended afterwards:

* J. Narayan, S. K. Shukla, and T. C. Clancy, “A Survey of Automatic Protocol Reverse Engineering Tools,” ACM Computing Surveys, vol. 48, no. 3, pp. 1–26, Feb. 2016, doi: 10.1145/2840724. [PDF](https://www.researchgate.net/profile/Sandeep_Shukla6/publication/287106642_A_Survey_of_Automatic_Protocol_Reverse_Engineering_Tools/links/5773948208ae1b18a7ddff91/A-Survey-of-Automatic-Protocol-Reverse-Engineering-Tools.pdf)
* J. Duchêne, C. Le Guernic, E. Alata, V. Nicomette, and M. Kaâniche, “State of the art of network protocol reverse engineering tools,” Journal of Computer Virology and Hacking Techniques, vol. 14, no. 1, pp. 53–68, Feb. 2018, doi: 10.1007/s11416-016-0289-8. [PDF](https://hal.inria.fr/hal-01496958/document)
* B. D. Sija, Y.-H. Goo, K.-S. Shim, H. Hasanova, and M.-S. Kim, “A Survey of Automatic Protocol Reverse Engineering Approaches, Methods, and Tools on the Inputs and Outputs View,” Security and Communication Networks, vol. 2018, pp. 1–17, 2018, doi: 10.1155/2018/8370341. [PDF](https://downloads.hindawi.com/journals/scn/2018/8370341.pdf)

Furthermore, there is a very extensive surveys which focuses on the methods and approaches of PRE tools that are based on network traces. The work of Kleber et al. is an excellent starting point to see what was already tried and for which use cases a method is working best.

* S. Kleber, L. Maile, and F. Kargl, “Survey of Protocol Reverse Engineering Algorithms: Decomposition of Tools for Static Traffic Analysis,” IEEE Communications Surveys & Tutorials, vol. 21, no. 1, pp. 526–561, 2019, doi: 10.1109/COMST.2018.2867544. [PDF](https://oparu.uni-ulm.de/xmlui/bitstream/handle/123456789/11078/COMST2867544.pdf)

Please help extending this collection by adding papers to the `tools.ods`.


# Table of Contents

* [Overview](#overview-)
* [Input and Output](#input-and-output-)
* [Tested protocols](#tested-protocols-)
* [Source code](#source-code-)
* [References](#references-)


# Overview [&uarr;](#table-of-contents)

| Name | Year | Approach used |
|------|------|---------------|
| PIP [[1]](#1) | 2004 | Keyword detection and Sequence alignment based on Needleman and Wunsch 1970 and Smith and Waterman 1981; this approach was applied and extended by many following papers |
| GAPA [[2]](#2) | 2005 | Protocol analyzer and open language that uses the protocol analyzer specification Spec → it is meant to be integrated in monitoring and analyzing tools |
| ScriptGen [[3]](#3) | 2005 | Grouping and clustering messages, find edges from clusters to clusters for being able to replay messages once a similar message arrives |
| RolePlayer [[4]](#4) | 2006 | Byte-wise sequence alignment (find variable fields in messages) and clustering with FSM simplification |
| Ma et al. [[5]](#5) | 2006 | Please review |
| FFE/x86 [[6]](#6) | 2006 | Please review |
| Replayer [[7]](#7) | 2006 | Please review |
| Discoverer [[8]](#8) | 2007 | Tokenization of messages, recursive clustering to find formats, merge similar formats |
| Polyglot [[9]](#9) | 2007 | Dynamic taint-analysis |
| PEXT [[10]](#10) | 2007 | Message clustering for creating FSM graph and simplify FSM graph |
| Rosetta [[11]](#11) | 2007 | Please review |
| AutoFormat [[12]](#12) | 2008 | Dynamic taint-analysis |
| Tupni [[13]](#13) | 2008 | Dynamic taint-analysis; look for loops to identify boundaries within messages |
| Boosting [[14]](#14) | 2008 | Please review |
| ConfigRE [[15]](#15) | 2008 | Please review |
| ReFormat [[16]](#16) | 2009 | Dynamic taint-analysis, especially targeting encrypted protocols by looking for bitwise and arithmetic operations |
| Prospex [[17]](#17) | 2009 | Dynamic taint-analysis with following message clustering, optionally provides fuzzing candidates for Peach fuzzer |
| Xiao et al. [[18]](#18) | 2009 | Please review |
| Trifilo et al. [[19]](#19) | 2009 | Measure byte-wise variances in aligned messages |
| Antunes and Neves [[20]](#20) | 2009 | Please review |
| Dispatcher [[21]](#21) | 2009 | Dynamic taint-analysis (successor of Polyglot using send instead of received messages) |
| Fuzzgrind [[22]](#22) | 2009 | Please review |
| REWARDS [[23]](#23) | 2010 | Please review |
| MACE [[24]](#24) | 2010 | Please review |
| Whalen et al. [[25]](#25) | 2010 | Please review |
| AutoFuzz [[26]](#26) | 2010 | Please review |
| ReverX [[27]](#27) | 2011 | Speech recognition (thus only for text-based protocols) to find carriage returns and spaces, afterwards looking for frequencies of keywords; multiple partial FSMs are merged and simplified to get PFSM |
| Veritas [[28]](#28) | 2011 | Identifiying keywords, clustering and transition probability → probabilistic protocol state machine |
| Biprominer [[29]](#29) | 2011 | Statistical analysis including three phases, learning phase, labeling phase and transition probability model building phase. See [this figure](img/biprominer.png). |
| ASAP [[30]](#30) | 2011 | Please review |
| Howard [[31]](#31) | 2011 | Please review |
| ProDecoder [[32]](#32) | 2012 | Successor of Biprominer which also addresses text-based protocols; two-phases are used: first apply Biprominer, second use Needleman-Wunsch for alignment |
| Zhang et al. [[33]](#33) | 2012 | Please review |
| Netzob [[34]](#34) | 2012 | See [this figure](https://github.com/netzob/netzob/blob/4a72c0cbd6d1e7b997b2b8ad170b7a38e400dfca/netzob/doc/documentation/source/netzob_archi.png) |
| PRISMA [[35]](#35) | 2012 | Please review, follow-up paper/project to ASAP |
| ARTISTE [[36]](#36) | 2012 | Please review |
| Wang et al. [[37]](#37) | 2013 | Capturing of data, identifying frames and inferring the format by looking and frequency of frames and doing association analysis (using Apriori and FP-Growth). |
| Laroche et al. [[38]](#38) | 2013 | Please review |
| AutoReEngine [[39]](#39) | 2013 | Apriori Algorithm (based on Agrawal/Srikant 1994). Identify fields and keywords by considering the amount of occurrences. Message formats are considered as series of keywords. State machines are derived from labeled messages or frequent subsequences. See [this figure](img/autoreengine.png) for clarification. |
| Dispatcher2 [[40]](#40) | 2013 | Please review |
| ProVeX [[41]](#41) | 2013 | Identify Botnet traffic and try to infer the botnet type by using signatures |
| Meng et al. [[42]](#42) | 2014 | Please review |
| AFL [[43]](#43) | 2014 | Please review |
| Proword [[44]](#44) | 2014 | Please review |
| ProGraph [[45]](#45) | 2015 | Please review |
| FieldHunter [[46]](#46) | 2015 | Please review |
| RS Cluster [[47]](#47) | 2015 | Please review |
| UPCSS [[48]](#48) | 2015 | Please review |
| ARGOS [[49]](#49) | 2015 | Please review |
| PULSAR [[50]](#50) | 2015 | Reverse engineer network protocols with the aim to fuzz them with thus knowledge |
| Li et al. [[51]](#51) | 2015 | Please review |
| Cai et al. [[52]](#52) | 2016 | Please review |
| WASp [[53]](#53) | 2016 | Pcap files are provided with context information (i.e. known MAC address), then grouping and analysing (looking for CRC, N-gram, Entropy, Features, Ranges), afterwards report creation based on scoring. |
| PRE-Bin [[54]](#54) | 2016 | Please review |
| Xiao et al. [[55]](#55) | 2016 | Please review |
| PowerShell [[56]](#56) | 2017 | Please review |
| ProPrint [[57]](#57) | 2017 | Please review |
| ProHacker [[58]](#58) | 2017 | Please review |
| Esoul and Walkinshaw [[59]](#59) | 2017 | Please review |
| PREUGI [[60]](#60) | 2017 | Please review |
| NEMESYS [[61]](#61) | 2018 | Please review |
| Goo et al. [[62]](#62) | 2019 | Apriori based: Finding „frequent contiguous common subsequences“ via new Contiguous Sequential Pattern (CSP) algorithm which is based on Generalized Sequential Pattern (GSP) and other Apriori algorithms. CSP is used three times hierarchically to extract different information/fields based on previous results. |
| Universal Radio Hacker [[63]](#63) | 2019 | Physical layer based analysis of proprietary wireless protocols considering wireless specific properties like Received Signal Strength Indicator (RSSI) and using statistical methods |
| Luo et al. [[64]](#64) | 2019 | From abstract: “[…] this study proposes a type-aware approach to message clustering guided by type information. The approach regards a message as a combination of n-grams, and it employs the Latent Dirichlet Allocation (LDA) model to characterize messages with types and n-grams via inferring the type distribution of each message.” |
| Sun et al. [[65]](#65) | 2019 | Please review |
| Yang et al. [[66]](#66) | 2020 | Using deep-learning (LSTM-FCN) for reversing binary protocols |
| Sun et al. [[67]](#67) | 2020 | "To measure format similarity of unknown protocol messages in a proper granularity, we propose relative measurements, Token Format Distance (TFD) and Message Format Distance (MFD), based on core rules of Augmented Backus-Naur Form (ABND)." for clustering process Silhouette Coefficient and Dunn Index are used. density based cluster algorithm DBSCAN is used for clustering of messages |
| Shim et al. [[68]](#68) | 2020 | Follow up on Goo et al. 2019 |
| IPART [[69]](#69) | 2020 | Using extended voting expert algorithm to infer boundaries of fields, otherwise using three phase which are tokenizing, classifying and clustering. |

# Input and Output [&uarr;](#table-of-contents)

NetT: input is a network trace (e.g. pcap)<br />
ExeT: input is an execution trace (code/binary at hand)<br />
PF: output is protocol format (describing the syntax)<br />
PFSM: output is protocol finite state machine (describing semantic/sequential logic)<br />

| Name | Year | NetT | ExeT | PF | PFSM | Other Output |
|------|------|------|------|----|------|--------------|
| PIP [[1]](#1) | 2004 | &#10004; |  |  |  | Keywords/ fields |
| GAPA [[2]](#2) | 2005 |  | &#10004; | &#10004; | &#10004; |  |
| ScriptGen [[3]](#3) | 2005 | &#10004; |  |  |  | Dialogs/scripts (for replaying) |
| RolePlayer [[4]](#4) | 2006 | &#10004; |  |  |  | Dialogs/scripts |
| Ma et al. [[5]](#5) | 2006 | &#10004; |  |  |  | App-identification |
| FFE/x86 [[6]](#6) | 2006 |  | &#10004; |  |  |  |
| Replayer [[7]](#7) | 2006 |  | &#10004; |  |  |  |
| Discoverer [[8]](#8) | 2007 | &#10004; |  | &#10004; |  |  |
| Polyglot [[9]](#9) | 2007 |  | &#10004; | &#10004; |  |  |
| PEXT [[10]](#10) | 2007 |  | &#10004; |  | &#10004; |  |
| Rosetta [[11]](#11) | 2007 |  | &#10004; |  |  |  |
| AutoFormat [[12]](#12) | 2008 |  | &#10004; | &#10004; |  |  |
| Tupni [[13]](#13) | 2008 |  | &#10004; | &#10004; |  |  |
| Boosting [[14]](#14) | 2008 | &#10004; |  |  |  | Field(s) |
| ConfigRE [[15]](#15) | 2008 |  | &#10004; |  |  |  |
| ReFormat [[16]](#16) | 2009 |  | &#10004; | &#10004; |  |  |
| Prospex [[17]](#17) | 2009 | &#10004; | &#10004; | &#10004; | &#10004; |  |
| Xiao et al. [[18]](#18) | 2009 |  | &#10004; |  | &#10004; |  |
| Trifilo et al. [[19]](#19) | 2009 | &#10004; |  |  | &#10004; |  |
| Antunes and Neves [[20]](#20) | 2009 | &#10004; |  |  | &#10004; |  |
| Dispatcher [[21]](#21) | 2009 |  | &#10004; |  |  | C&C malware |
| Fuzzgrind [[22]](#22) | 2009 |  | &#10004; |  |  |  |
| REWARDS [[23]](#23) | 2010 |  | &#10004; |  |  |  |
| MACE [[24]](#24) | 2010 |  | &#10004; |  |  |  |
| Whalen et al. [[25]](#25) | 2010 | &#10004; |  | &#10004; |  |  |
| AutoFuzz [[26]](#26) | 2010 | &#10004; |  | &#10004; | &#10004; |  |
| ReverX [[27]](#27) | 2011 | &#10004; |  | &#10004; | &#10004; |  |
| Veritas [[28]](#28) | 2011 | &#10004; |  |  | &#10004; |  |
| Biprominer [[29]](#29) | 2011 | &#10004; |  | &#10004; | &#10004; |  |
| ASAP [[30]](#30) | 2011 | &#10004; |  |  |  | Semantics |
| Howard [[31]](#31) | 2011 |  | &#10004; |  |  |  |
| ProDecoder [[32]](#32) | 2012 | &#10004; |  | &#10004; |  |  |
| Zhang et al. [[33]](#33) | 2012 | &#10004; |  |  | &#10004; |  |
| Netzob [[34]](#34) | 2012 | &#10004; | &#10004; | &#10004; | &#10004; |  |
| PRISMA [[35]](#35) | 2012 | &#10004; |  |  |  |  |
| ARTISTE [[36]](#36) | 2012 |  | &#10004; |  |  |  |
| Wang et al. [[37]](#37) | 2013 | &#10004; |  | &#10004; |  |  |
| Laroche et al. [[38]](#38) | 2013 | &#10004; |  |  | &#10004; |  |
| AutoReEngine [[39]](#39) | 2013 | &#10004; |  | &#10004; | &#10004; |  |
| Dispatcher2 [[40]](#40) | 2013 |  | &#10004; |  |  | C&C malware |
| ProVeX [[41]](#41) | 2013 | &#10004; |  |  |  | Signatures |
| Meng et al. [[42]](#42) | 2014 | &#10004; |  |  | &#10004; |  |
| AFL [[43]](#43) | 2014 |  | &#10004; |  |  |  |
| Proword [[44]](#44) | 2014 |  |  |  |  |  |
| ProGraph [[45]](#45) | 2015 | &#10004; |  | &#10004; |  |  |
| FieldHunter [[46]](#46) | 2015 | &#10004; |  |  |  | Fields |
| RS Cluster [[47]](#47) | 2015 | &#10004; |  |  |  | Grouped-messages |
| UPCSS [[48]](#48) | 2015 | &#10004; |  |  |  | Proto-classification |
| ARGOS [[49]](#49) | 2015 |  | &#10004; |  |  |  |
| PULSAR [[50]](#50) | 2015 |  |  |  |  |  |
| Li et al. [[51]](#51) | 2015 | &#10004; |  | &#10004; |  |  |
| Cai et al. [[52]](#52) | 2016 | &#10004; |  | &#10004; |  |  |
| WASp [[53]](#53) | 2016 | &#10004; |  | &#10004; |  | scored analysis reports, spoofing candidates |
| PRE-Bin [[54]](#54) | 2016 | &#10004; |  | &#10004; |  |  |
| Xiao et al. [[55]](#55) | 2016 | &#10004; |  | &#10004; |  |  |
| PowerShell [[56]](#56) | 2017 | &#10004; |  |  |  | Dialogs/scripts |
| ProPrint [[57]](#57) | 2017 | &#10004; |  |  |  | Fingerprints |
| ProHacker [[58]](#58) | 2017 | &#10004; |  |  |  | Keywords |
| Esoul and Walkinshaw [[59]](#59) | 2017 |  |  |  |  |  |
| PREUGI [[60]](#60) | 2017 | &#10004; |  |  | &#10004; |  |
| NEMESYS [[61]](#61) | 2018 | &#10004; |  | &#10004; |  |  |
| Goo et al. [[62]](#62) | 2019 | &#10004; |  | &#10004; | &#10004; |  |
| Universal Radio Hacker [[63]](#63) | 2019 | &#10004; |  | &#10004; |  |  |
| Luo et al. [[64]](#64) | 2019 |  |  |  |  |  |
| Sun et al. [[65]](#65) | 2019 |  |  |  |  |  |
| Yang et al. [[66]](#66) | 2020 | &#10004; |  | &#10004; |  |  |
| Sun et al. [[67]](#67) | 2020 |  |  |  |  |  |
| Shim et al. [[68]](#68) | 2020 | &#10004; |  | &#10004; |  |  |
| IPART [[69]](#69) | 2020 | &#10004; |  | &#10004; |  |  |

# Tested protocols [&uarr;](#table-of-contents)

| Name | Year | Text-based | Binary-based | Hybrid | Other Protocols |
|------|------|------------|--------------|--------|-----------------|
| PIP [[1]](#1) | 2004 | HTTP |  |  |  |
| GAPA [[2]](#2) | 2005 | HTTP |  |  |  |
| ScriptGen [[3]](#3) | 2005 | HTTP | NetBIOS |  | DCE |
| RolePlayer [[4]](#4) | 2006 | HTTP, FTP, SMTP, NFS, TFTP | DNS, BitTorrent, QQ, NetBios | SMB, CIFS |  |
| Ma et al. [[5]](#5) | 2006 | HTTP, FTP, SMTP, HTTPS (TCP-Protos) | DNS, NetBIOS, SrvLoc (UDP-Protos) |  |  |
| FFE/x86 [[6]](#6) | 2006 |  |  |  |  |
| Replayer [[7]](#7) | 2006 |  |  |  |  |
| Discoverer [[8]](#8) | 2007 | HTTP | RPC | SMB, CIFS |  |
| Polyglot [[9]](#9) | 2007 | HTTP, Samba, ICQ | DNS, IRC |  |  |
| PEXT [[10]](#10) | 2007 | FTP |  |  |  |
| Rosetta [[11]](#11) | 2007 |  |  |  |  |
| AutoFormat [[12]](#12) | 2008 | HTTP, SIP | DHCP, RIP, OSPF | SMB, CIFS |  |
| Tupni [[13]](#13) | 2008 | HTTP, FTP | RPC, DNS, TFTP |  | WMF, BMP, JPG, PNG, TIF |
| Boosting [[14]](#14) | 2008 |  | DNS |  |  |
| ConfigRE [[15]](#15) | 2008 |  |  |  |  |
| ReFormat [[16]](#16) | 2009 | HTTP, MIME | IRC |  | One unknown protocol |
| Prospex [[17]](#17) | 2009 | SMTP, SIP | SMB |  | Agobot (C&C) |
| Xiao et al. [[18]](#18) | 2009 | HTTP, FTP, SMTP |  |  |  |
| Trifilo et al. [[19]](#19) | 2009 |  | TCP, DHCP, ARP, KAD |  |  |
| Antunes and Neves [[20]](#20) | 2009 | FTP |  |  |  |
| Dispatcher [[21]](#21) | 2009 | HTTP, FTP, ICQ | DNS |  |  |
| Fuzzgrind [[22]](#22) | 2009 |  |  |  |  |
| REWARDS [[23]](#23) | 2010 |  |  |  |  |
| MACE [[24]](#24) | 2010 |  |  |  |  |
| Whalen et al. [[25]](#25) | 2010 |  |  |  |  |
| AutoFuzz [[26]](#26) | 2010 |  |  |  |  |
| ReverX [[27]](#27) | 2011 | FTP |  |  |  |
| Veritas [[28]](#28) | 2011 | SMTP | PPLIVE, XUNLEI |  |  |
| Biprominer [[29]](#29) | 2011 |  | XUNLEI, QQLive, SopCast |  |  |
| ASAP [[30]](#30) | 2011 | HTTP, FTP, IRC, TFTP |  |  |  |
| Howard [[31]](#31) | 2011 |  |  |  |  |
| ProDecoder [[32]](#32) | 2012 | SMTP, SIP | SMB |  |  |
| Zhang et al. [[33]](#33) | 2012 | HTTP, SNMP, ISAKMP |  |  |  |
| Netzob [[34]](#34) | 2012 | FTP, Samba | SMB |  | Unknown P2P & VoIP protocol |
| PRISMA [[35]](#35) | 2012 |  |  |  |  |
| ARTISTE [[36]](#36) | 2012 |  |  |  |  |
| Wang et al. [[37]](#37) | 2013 | ICMP | ARP |  |  |
| Laroche et al. [[38]](#38) | 2013 | FTP | DHCP |  |  |
| AutoReEngine [[39]](#39) | 2013 | HTTP, FTP, SMTP, POP3 | DNS, NetBIOS |  |  |
| Dispatcher2 [[40]](#40) | 2013 | HTTP, FTP, ICQ | DNS | SMB |  |
| ProVeX [[41]](#41) | 2013 | HTTP, SMTP, IMAP | DNS, VoIP, XMPP |  | Malware Family Protocols |
| Meng et al. [[42]](#42) | 2014 |  | TCP, ARP |  |  |
| AFL [[43]](#43) | 2014 |  |  |  |  |
| Proword [[44]](#44) | 2014 |  |  |  |  |
| ProGraph [[45]](#45) | 2015 | HTTP | DNS, BitTorrent, WeChat |  |  |
| FieldHunter [[46]](#46) | 2015 | MSNP | DNS |  | SopCast, Ramnit |
| RS Cluster [[47]](#47) | 2015 | FTP, SMTP, POP3, HTTPS | DNS, XunLei, BitTorrent, BitSpirit, QQ, eMule |  | MSSQL, Kugoo, PPTV |
| UPCSS [[48]](#48) | 2015 | HTTP, FTP, SMTP, POP3, IMAP | DNS, SSL, SSH | SMB |  |
| ARGOS [[49]](#49) | 2015 |  |  |  |  |
| PULSAR [[50]](#50) | 2015 |  |  |  |  |
| Li et al. [[51]](#51) | 2015 |  |  |  |  |
| Cai et al. [[52]](#52) | 2016 | HTTP, SSDP | DNS, BitTorrent, QQ, NetBios |  |  |
| WASp [[53]](#53) | 2016 |  |  |  | IEEE 802.15.4 proprietary protocols, Smart plug & PSD systems |
| PRE-Bin [[54]](#54) | 2016 |  |  |  |  |
| Xiao et al. [[55]](#55) | 2016 |  |  |  |  |
| PowerShell [[56]](#56) | 2017 |  | ARP, OSPF, DHCP, STP |  | CDP/DTP/VTP, HSRP, LLDP, LLMNR, mDNS, NBNS, VRRP |
| ProPrint [[57]](#57) | 2017 |  |  |  |  |
| ProHacker [[58]](#58) | 2017 |  |  |  |  |
| Esoul and Walkinshaw [[59]](#59) | 2017 |  |  |  |  |
| PREUGI [[60]](#60) | 2017 |  |  |  |  |
| NEMESYS [[61]](#61) | 2018 |  |  |  |  |
| Goo et al. [[62]](#62) | 2019 | HTTP | DNS |  |  |
| Universal Radio Hacker [[63]](#63) | 2019 |  |  |  | proprietary wireless protocols of IoT devices |
| Luo et al. [[64]](#64) | 2019 |  |  |  |  |
| Sun et al. [[65]](#65) | 2019 |  |  |  |  |
| Yang et al. [[66]](#66) | 2020 |  | IPv4, TCP |  |  |
| Sun et al. [[67]](#67) | 2020 |  |  |  |  |
| Shim et al. [[68]](#68) | 2020 | FTP | Modbus/TCP, Ethernet/IP |  |  |
| IPART [[69]](#69) | 2020 |  | Modbus, IEC104, Ethernet/IP |  |  |

# Source Code [&uarr;](#table-of-contents)

Most papers do not provide the code used in the research. For the following papers exists (example) code.<br/>
| Name | Year | Source Code |
|------|------|-------------|
| PIP [[1]](#1) | 2004 | https://web.archive.org/web/20090416234849/http://4tphi.net/~awalters/PI/PI.html |
| ReverX [[27]](#27) | 2011 | https://github.com/jasantunes/reverx |
| Netzob [[34]](#34) | 2012 | https://github.com/netzob/netzob |
| PRISMA [[35]](#35) | 2012 | https://github.com/tammok/PRISMA/ |
| PULSAR [[50]](#50) | 2015 | https://github.com/hgascon/pulsar |
| NEMESYS [[61]](#61) | 2018 | https://github.com/vs-uulm/nemesys |
| Universal Radio Hacker [[63]](#63) | 2019 | https://github.com/jopohl/urh |

# References [&uarr;](#table-of-contents)

#### [1]
M. Beddoe, “The protocol informatics project,” 2004, http://www.4tphi.net/∼awalters/PI/PI.html. [PDF](http://www.4tphi.net/~awalters/PI/pi.pdf)
#### [2]
N. Borisov, D. J. Brumley, H. J. Wang, J. Dunagan, P. Joshi, and C. Guo, “Generic application-level protocol analyzer and its language,” MSR Technical Report MSR-TR-2005-133, 2005. [PDF](http://www.academia.edu/download/31148072/2005-133.pdf)
#### [3]
C. Leita, K. Mermoud, and M. Dacier, “ScriptGen: an automated script generation tool for Honeyd,” in Proceedings of the 21st Annual Computer Security Applications Conference (ACSAC ’05), pp. 203–214, Tucson, Ariz, USA, December 2005. [PDF](https://www.researchgate.net/profile/Marc_Dacier/publication/4207362_ScriptGen_an_automated_script_generation_tool_for_Honeyd/links/02e7e52f3691fd9dbb000000/ScriptGen-an-automated-script-generation-tool-for-Honeyd.pdf)
#### [4]
W. Cui, V. Paxson, N. C. Weaver, and R. H. Katz, “Protocolindependent adaptive replay of application dialog,” in Proceedings of the 13th Symposium on Network and Distributed System Security (NDSS ’06), 2006. [PDF](https://www.ndss-symposium.org/wp-content/uploads/2017/09/Protocol-Independent-Adaptive-Replay-of-Application-Dialog-Weidong-Cui.pdf)
#### [5]
J. Ma, K. Levchenko, C. Kreibich, S. Savage, and G. Voelker, “Automatic protocol inference: unexpected means of identifying protocols,” UCSD Computer Science Technical Report CS2006-0850, 2006. [PDF](http://www.academia.edu/download/38268/2q7zdptm5klmgg2h0g9.pdf)
#### [6]
Lim, J., Reps, T., Liblit, B.: Extracting output formats from executables. In: 13th Working Conference on Reverse Engineering, 2006. WCRE ’06, pp. 167–178. IEEE, Benevento (2006). doi:10.1109/WCRE.2006.29 [PDF](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.138.3603&rep=rep1&type=pdf)
#### [7]
Cui, W., Paxson, V., Weaver, N., Katz, R.H.: Protocol-independent adaptive replay of application dialog. In: Proceedings of the 13th Annual Network and Distributed System Security Symposium (NDSS). Internet Society, San Diego (2006). http://research.microsoft.com/apps/pubs/default.aspx?id=153197
#### [8]
W. Cui, J. Kannan, and H. J. Wang, “Discoverer: Automatic protocol reverse engineering from network traces.,” in USENIX security symposium, 2007, pp. 1–14.  [PDF](https://www.usenix.org/event/sec07/tech/full_papers/cui/cui.pdf)
#### [9]
J. Caballero, H. Yin, Z. Liang, and D. Song, “Polyglot: automatic extraction of protocol message format using dynamic binary analysis,” in Proceedings of the 14th ACM Conference on Computer and Communications Security (CCS ’07), pp. 317–329, ACM, November 2007. [PDF](https://people.eecs.berkeley.edu/~dawnsong/papers/2007%20p317-caballero.pdf)
#### [10]
M. Shevertalov and S. Mancoridis, “A reverse engineering tool for extracting protocols of networked applications,” in Proceedings of the 14th Working Conference on Reverse Engineering (WCRE ’07), pp. 229–238, October 2007.
#### [11]
Caballero, J., Song, D.: Rosetta: Extracting Protocol Semantics Using Binary Analysis with Applications to Protocol Replay and NAT Rewriting. Technical Report CMU-CyLab-07-014, Carnegie Mellon University, Pittsburgh (2007)
#### [12]
Z. Lin, X. Jiang, D. Xu, and X. Zhang, “Automatic protocol format reverse engineering through context-aware monitored execution,” in Proceedings of the 15th Symposium on Network and  Distributed System Security (NDSS ’08), February 2008. [PDF](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.120.2651&rep=rep1&type=pdf)
#### [13]
W. Cui, M. Peinado, K. Chen, H. J. Wang, and L. Irun-Briz, “Tupni: automatic reverse engineering of input formats,” in Proceedings of the 15th ACM Conference on Computer and Communications Security (CCS ’08), pp. 391–402, ACM, Alexandria, Va, USA, October 2008. [PDF](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/tupni-ccs08.pdf)
#### [14]
K. Gopalratnam, S. Basu, J. Dunagan, and H. J. Wang, “Automatically extracting fields from unknown network protocols,” in Proceedings of the 15th Symposium on Network and Distributed System Security (NDSS ’08), 2008. [PDF](http://www.nicemice.net/helen/papers/sysml-Gopalratnam.pdf)
#### [15]
Wang, R., Wang, X., Zhang, K., Li, Z.: Towards automatic reverse engineering of software security configurations. In: Proceedings of the 15th ACM Conference on Computer and Communications Security, CCS ’08, pp. 245–256. ACM, Limerick (2008). doi:10.1145/1455770.1455802
#### [16]
Z. Wang, X. Jiang, W. Cui, X. Wang, and M. Grace, “ReFormat: automatic reverse engineering of encrypted messages,” in Computer Security—ESORICS 2009. ESORICS 2009, M. Backes and P. Ning, Eds., vol. 5789 of Lecture Notes in Computer Science, pp. 200–215, Springer, Berlin, Germany, 2009. [PDF](https://link.springer.com/content/pdf/10.1007/978-3-642-04444-1_13.pdf)
#### [17]
P. M. Comparetti, G. Wondracek, C. Kruegel, and E. Kirda, “Prospex: protocol specification extraction,” in Proceedings of the 30th IEEE Symposium on Security and Privacy, pp. 110–125, Berkeley, Calif, USA, May 2009. [PDF](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.720.3272&rep=rep1&type=pdf)
#### [18]
M.-M. Xiao, S.-Z. Yu, and Y. Wang, “Automatic network protocol automaton extraction,” in Proceedings of the 3rd International Conference on Network and System Security (NSS ’09), pp. 336–343, October 2009.
#### [19]
A. Trifilo, S. Burschka, and E. Biersack, “Traffic to protocol reverse engineering,” in Proceedings of the IEEE Symposium on Computational Intelligence for Security and Defense Applications, pp. 1–8, July 2009. [PDF](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.161.2189&rep=rep1&type=pdf)
#### [20]
J. Antunes and N. Neves, “Building an automaton towards reverse protocol engineering,” 2009, http://www.di.fc.ul.pt/∼nuno/PAPERS/INFORUM09.pdf.
#### [21]
J. Caballero, P. Poosankam, C. Kreibich, and D. Song, “Dispatcher: enabling active botnet infiltration using automatic protocol reverse-engineering,” in Proceedings of the 16th ACM Conference on Computer and Communications Security (CCS ’09), pp. 621–634, ACM, Chicago, Ill, USA, November 2009. [PDF](https://people.eecs.berkeley.edu/~dawnsong/papers/2009%20Dispatcher.pdf)
#### [22]
Campana, G.: Fuzzgrind: an automatic fuzzing tool. In: Hack. lu. Hack. lu, Luxembourg (2009)
#### [23]
Lin, Z., Zhang, X., Xu, D.: Automatic reverse engineering of data structures from binary execution. In: Proceedings of the 17th Annual Network and Distributed System Security Symposium (NDSS). Internet Society, San Diego (2010)
#### [24]
Cho, C.Y., Babi D., Shin, E.C.R., Song, D.: Inference and analysis of formal models of botnet command and control protocols. In: Proceedings of the 17th ACM Conference on Computer and Communications Security, CCS ’10, pp. 426–439. ACM, New York, NY (2010). doi:10.1145/1866307.1866355
Cho, C.Y., Babi, D., Poosankam, P., Chen, K.Z., Wu, E.X., Song, D.: MACE: model-inference-assisted concolic exploration for protocol and vulnerability discovery. In: Proceedings of the 20th USENIX Conference on Security, SEC’11, p. 19. USENIX Association, Berkeley, CA (2011)
#### [25]
S. Whalen, M. Bishop, and J. P. Crutchfield, “Hidden Markov Models for Automated Protocol Learning,” in Security and Privacy in Communication Networks, vol. 50, S. Jajodia and J. Zhou, Eds. Berlin, Heidelberg: Springer Berlin Heidelberg, 2010, pp. 415–428.  [PDF](http://nob.cs.ucdavis.edu/bishop/papers/2010-securecomm/markov.pdf)
#### [26]
S. Gorbunov and A. Rosenbloom, “Autofuzz: Automated network protocol fuzzing framework,” IJCSNS, vol. 10, no. 8, p. 239, 2010.  [PDF](people.csail.mit.edu/sergeyg/publications/autofuzz.pdf)
#### [27]
J. Antunes, N. Neves, and P. Verissimo, “Reverse engineering of protocols from network traces,” in Proceedings of the 18th Working Conference on Reverse Engineering (WCRE ’11), pp. 169–178, October 2011. [PDF](https://www.researchgate.net/profile/Joao_Antunes3/publication/221200255_Reverse_Engineering_of_Protocols_from_Network_Traces/links/0fcfd50c3eb9574ac4000000.pdf)
#### [28]
Y. Wang, Z. Zhang, D. D. Yao, B. Qu, and L. Guo, “Inferring protocol state machine from network traces: a probabilistic approach,” in Proceedings of the 9th Applied Cryptography and Network Security International Conference (ACNS ’11), pp. 1–18, 2011.
#### [29]
Y. Wang, X. Li, J. Meng, Y. Zhao, Z. Zhang, and L. Guo, “Biprominer: automatic mining of binary protocol features,” in Proceedings of the 12th International Conference on Parallel and Distributed Computing, Applications and Technologies (PDCAT ’11), pp. 179–184, October 2011.
#### [30]
T. Krueger, N. Krmer, and K. Rieck, “Asap: automatic semantics-aware analysis of network payloads,” in Proceedings of the ECML/PKDD, 2011. [PDF](https://oar.tib.eu/jspui/bitstream/123456789/2288/1/664831966.pdf)
#### [31]
Slowinska, A., Stancescu, T., Bos, H.: Howard: a dynamic excavator for reverse engineering data structures. In: Proceedings of the 18th Annual Network and Distributed System Security Symposium (NDSS). Internet Society, San Diego (2011)
#### [32]
Y. Wang, X. Yun, M. Z. Shafiq et al., “A semantics aware approach to automated reverse engineering unknown protocols,” in Proceedings of the 20th IEEE International Conference on Network Protocols (ICNP ’12), pp. 1–10, IEEE, Austin, Tex, USA, November 2012. [PDF](https://yaogroup.cs.vt.edu/papers/ICNP-12.pdf)
#### [33]
Z. Zhang, Q.-Y. Wen, and W. Tang, “Mining protocol state machines by interactive grammar inference,” in Proceedings of the 2012 3rd International Conference on Digital Manufacturing and Automation (ICDMA ’12), pp. 524–527, August 2012.
#### [34]
G. Bossert, F. Guihéry, and G. Hiet, “Towards automated protocol reverse engineering using semantic information,” in Proceedings of the 9th ACM Symposium on Information, Computer and Communications Security, Kyoto, Japan, June 2014.
G. Bossert and F. Guihéry, “Reverse and simulate your enemy botnet C&C,” in Proceedings of the Mapping a P2P Botnet with Netzob, Black Hat 2012, Abu Dhabi, UAE, December 2012. [PDF](https://www.amossys.fr/upload/publication.pdf)
#### [35]
Krueger, T., Gascon, H., Krmer, N., Rieck, K.: Learning stateful models for network honeypots. In: Proceedings of the 5th ACM Workshop on Security and Artificial Intelligence, AISec ’12, pp. 37–48. ACM, New York, NY (2012). doi:10.1145/2381896.2381904
#### [36]
Caballero, J., Grieco, G., Marron, M., Lin, Z., Urbina, D.: ARTISTE: Automatic Generation of Hybrid Data Structure Signatures from Binary Code Executions. Technical Report TR-IMDEA-SW-2012-001, IMDEA Software Institute, Madrid (2012)
#### [37]
Y. Wang, N. Zhang, Y.-M. Wu, B.-B. Su, and Y.-J. Liao, “Protocol formats reverse engineering based on association rules in wireless environment,” in Proceedings of the 12th IEEE International Conference on Trust, Security and Privacy in Computing and Communications (TrustCom ’13), pp. 134–141, Melbourne, Australia, July 2013.
#### [38]
P. Laroche, A. Burrows, and A. N. Zincir-Heywood, “How far an evolutionary approach can go for protocol state analysis and discovery,” in Proceedings of the IEEE Congress on Evolutionary Computation (CEC ’13), pp. 3228–3235, June 2013.
#### [39]
J.-Z. Luo and S.-Z. Yu, “Position-based automatic reverse engineering of network protocols,” Journal of Network and Computer Applications, vol. 36, no. 3, pp. 1070–1077, 2013.
#### [40]
J. Caballero and D. Song, “Automatic protocol reverse-engineering: message format extraction and field semantics inference,” Computer Networks, vol. 57, no. 2, pp. 451–474, 2013. [PDF](http://www.academia.edu/download/47267446/j.comnet.2012.08.00320160715-7025-1uns1ji.pdf)
#### [41]
C. Rossow and C. J. Dietrich, “PROVEX: detecting botnets with encrypted command and control channels,” in Detection of Intrusions and Malware, and Vulnerability Assessment, Springer, 2013. [PDF](https://chrisdietri.ch/files/provex-dimva2013.pdf)
#### [42]
F. Meng, Y. Liu, C. Zhang, T. Li, and Y. Yue, “Inferring protocol state machine for binary communication protocol,” in Proceedings of the IEEE Workshop on Advanced Research and Technology in Industry Applications (WARTIA ’14), pp. 870–874, September 2014.
#### [43]
Zalewski, M.: American Fuzzy Loop. http://lcamtuf.coredump.cx/afl/technical_details.txt
#### [44]
Z. Zhang, Z. Zhang, P. P. C. Lee, Y. Liu, and G. Xie, “ProWord: An unsupervised approach to protocol feature word extraction,” in IEEE INFOCOM 2014 - IEEE Conference on Computer Communications, Toronto, ON, Canada, Apr. 2014, pp. 1393–1401, doi: 10.1109/INFOCOM.2014.6848073.  [PDF](http://adslab.cse.cuhk.edu.hk/pubs/infocom14proword.pdf)
#### [45]
Q. Huang, P. P. C. Lee, and Z. Zhang, “Exploiting intrapacket dependency for fine-grained protocol format inference,” in Proceedings of the 14th IFIP Networking Conference (NETWORKING ’15), Toulouse, France, May 2015.
#### [46]
I. Bermudez, A. Tongaonkar, M. Iliofotou, M. Mellia, and M. M. Munafo, “Automatic protocol field inference for deeper protocol understanding,” in Proceedings of the 14th IFIP Networking Conference (Networking ’15), pp. 1–9, May 2015. [PDF](http://dl.ifip.org/db/conf/networking/networking2015/1570062733.pdf)
#### [47]
J.-Z. Luo, S.-Z. Yu, and J. Cai, “Capturing uncertainty information and categorical characteristics for network payload grouping in protocol reverse engineering,” Mathematical Problems in Engineering, vol. 2015, Article ID 962974, 9 pages, 2015.
#### [48]
R. Lin, O. Li, Q. Li, and Y. Liu, “Unknown network protocol classification method based on semi supervised learning,” in Proceedings of the IEEE International Conference on Computer and Communications (ICCC ’15), pp. 300–308, Chengdu, China, October 2015.
#### [49]
Zeng, J., Lin, Z.: Towards automatic inference of kernel object semantics from binary code. In: 18th International Symposium, RAID 2015, vol. 9404, pp. 538–561. Springer, Kyoto (2015). doi:10.1007/978-3-319-26362-5
#### [50]
H. Gascon, C. Wressnegger, F. Yamaguchi, D. Arp, and K. Rieck, “Pulsar: Stateful Black-Box Fuzzing of Proprietary Network Protocols,” in Security and Privacy in Communication Networks, vol. 164, B. Thuraisingham, X. Wang, and V. Yegneswaran, Eds. Cham: Springer International Publishing, 2015, pp. 330–347.  [PDF](http://user.cs.uni-goettingen.de/~krieck/docs/2015-securecomm.pdf)
#### [51]
H. Li, B. Shuai, J. Wang, and C. Tang, “Protocol Reverse Engineering Using LDA and Association Analysis,” in 2015 11th International Conference on Computational Intelligence and Security (CIS), Shenzhen, China, Dec. 2015, pp. 312–316, doi: 10.1109/CIS.2015.83. 
#### [52]
J. Cai, J. Luo, and F. Lei, “Analyzing network protocols of application layer using hidden Semi-Markov model,” Mathematical Problems in Engineering, vol. 2016, Article ID 9161723, 14 pages, 2016.
#### [53]
K. Choi, Y. Son, J. Noh, H. Shin, J. Choi, and Y. Kim, “Dissecting customized protocols: automatic analysis for customized protocols based on IEEE 802.15.4,” in Proceedings of the 9th ACM Conference on Security and Privacy in Wireless and Mobile Networks, pp. 183–193, Darmstadt, Germany, July 2016. [PDF](https://koasas.kaist.ac.kr/bitstream/10203/215875/1/choi_wisec2016.pdf)
#### [54]
S. Tao, H. Yu, and Q. Li, “Bit‐oriented format extraction approach for automatic binary protocol reverse engineering,” IET Communications, vol. 10, no. 6, pp. 709–716, Apr. 2016, doi: 10.1049/iet-com.2015.0797.  [PDF](https://www.researchgate.net/profile/Si_Yu_Tao/publication/298803896_Bit-oriented_format_extraction_approach_for_automatic_binary_protocol_reverse_engineering/links/5cef30e64585153c3da53f0e/Bit-oriented-format-extraction-approach-for-automatic-binary-protocol-reverse-engineering.pdf)
#### [55]
M.-M. Xiao, S.-L. Zhang, and Y.-P. Luo, “Automatic network protocol message format analysis,” IFS, vol. 31, no. 4, pp. 2271–2279, Sep. 2016, doi: 10.3233/JIFS-169067. 
#### [56]
D. R. Fletcher Jr., Identifying Vulnerable Network Protocols with PowerShell, SANS Institute Reading Room site, 2017.
#### [57]
Y. Wang, X. Yun, Y. Zhang, L. Chen, and G. Wu, “A nonparametric approach to the automated protocol fingerprint inference,” Journal of Network and Computer Applications, vol. 99, pp. 1–9, 2017.
#### [58]
Y. Wang, X. Yun, Y. Zhang, L. Chen, and T. Zang, “Rethinking robust and accurate application protocol identification,” Computer Networks, vol. 129, pp. 64–78, 2017.
#### [59]
O. Esoul and N. Walkinshaw, “Using Segment-Based Alignment to Extract Packet Structures from Network Traces,” in 2017 IEEE International Conference on Software Quality, Reliability and Security (QRS), Prague, Czech Republic, Jul. 2017, pp. 398–409, doi: 10.1109/QRS.2017.49.  [PDF](https://leicester.figshare.com/articles/Using_Segment-Based_Alignment_to_Extract_Packet_Structures_from_Network_Traces/10236467/files/18473123.pdf)
#### [60]
M.-M. Xiao and Y.-P. Luo, “Automatic protocol reverse engineering using grammatical inference,” IFS, vol. 32, no. 5, pp. 3585–3594, Apr. 2017, doi: 10.3233/JIFS-169294. 
#### [61]
S. Kleber, H. Kopp, and F. Kargl, “{NEMESYS}: Network message syntax reverse engineering by analysis of the intrinsic structure of individual messages,” 2018.  [PDF](https://www.usenix.org/system/files/conference/woot18/woot18-paper-kleber.pdf)
#### [62]
Y.-H. Goo, K.-S. Shim, M.-S. Lee, and M.-S. Kim, “Protocol Specification Extraction Based on Contiguous Sequential Pattern Algorithm,” IEEE Access, vol. 7, pp. 36057–36074, 2019, doi: 10.1109/ACCESS.2019.2905353.  [PDF](https://ieeexplore.ieee.org/iel7/6287639/6514899/08667834.pdf)
#### [63]
J. Pohl and A. Noack, “Universal radio hacker: A suite for analyzing and attacking stateful wireless protocols,” Baltimore, MD, Aug. 2018, [Online]. Available: https://www.usenix.org/conference/woot18/presentation/pohl. 
J. Pohl and A. Noack, “Automatic wireless protocol reverse engineering,” Santa Clara, CA, Aug. 2019, [Online]. Available: https://www.usenix.org/conference/woot19/presentation/pohl.  [PDF](https://www.usenix.org/system/files/conference/woot18/woot18-paper-pohl.pdf)
#### [64]
X. Luo, D. Chen, Y. Wang, and P. Xie, “A Type-Aware Approach to Message Clustering for Protocol Reverse Engineering,” Sensors, vol. 19, no. 3, p. 716, Feb. 2019, doi: 10.3390/s19030716.  [PDF](https://www.mdpi.com/1424-8220/19/3/716/pdf)
#### [65]
F. Sun, S. Wang, C. Zhang, and H. Zhang, “Unsupervised field segmentation of unknown protocol messages,” Computer Communications, vol. 146, pp. 121–130, Oct. 2019, doi: 10.1016/j.comcom.2019.06.013. 
#### [66]
C. Yang, C. Fu, Y. Qian, Y. Hong, G. Feng, and L. Han, “Deep Learning-Based Reverse Method of Binary Protocol,” in Security and Privacy in Digital Economy, vol. 1268, S. Yu, P. Mueller, and J. Qian, Eds. Singapore: Springer Singapore, 2020, pp. 606–624. 
#### [67]
F. Sun, S. Wang, C. Zhang, and H. Zhang, “Clustering of unknown protocol messages based on format comparison,” Computer Networks, vol. 179, p. 107296, Oct. 2020, doi: 10.1016/j.comnet.2020.107296. 
#### [68]
K. Shim, Y. Goo, M. Lee, and M. Kim, “Clustering method in protocol reverse engineering for industrial protocols,” International Journal of Network Management, Jun. 2020, doi: 10.1002/nem.2126.  [PDF](https://nmlab.korea.ac.kr/publication/published.papers/2020/2020.06_Clustering_method_for_ICS-APRE-IJNM.pdf)
#### [69]
X. Wang, K. Lv, and B. Li, “IPART: an automatic protocol reverse engineering tool based on global voting expert for industrial protocols,” International Journal of Parallel, Emergent and Distributed Systems, vol. 35, no. 3, pp. 376–395, May 2020, doi: 10.1080/17445760.2019.1655740. 
