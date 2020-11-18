PRE-list
========

List of (automatic) protocol reverse engineering tools/methods/approaches for network protocols
<br/>This is a collection of 57 scientific papers about (automatic) protocol reverse engineering (PRE) methods and tools. The papers are categorized into different groups so that it is more easy to get an overview of existing solutions based on the problem you want to tackle.<br/>Please help extending this collection by using the `tools.ods`.


# Table of Contents

* [Overview](#overview-)
* [Input and Output](#input-and-output-)
* [Tested protocols](#tested-protocols-)
* [Source code](#source-code-)
* [References](#references-)


# Overview [&uarr;](#table-of-contents)

| Name | Year | NetT | ExeT | PF | PFSM | Other Output |
|------|------|------|------|----|------|--------------|
| PIP [[1]](#1) | 2004 | x |  |  |  | Keywords/ fields |
| GAPA [[2]](#2) | 2005 |  | x | x | x |  |
| ScriptGen [[3]](#3) | 2005 | x |  |  |  | Dialogs/scripts |
| RolePlayer [[4]](#4) | 2006 | x |  |  |  | Dialogs/scripts |
| Ma et al. [[5]](#5) | 2006 | x |  |  |  | App-identification |
| FFE/x86 [[6]](#6) | 2006 |  | x |  |  |  |
| Replayer [[7]](#7) | 2006 |  | x |  |  |  |
| Discoverer [[8]](#8) | 2007 | x |  | x |  |  |
| Polyglot [[9]](#9) | 2007 |  | x | x |  |  |
| PEXT [[10]](#10) | 2007 |  | x |  | x |  |
| Rosetta [[11]](#11) | 2007 |  | x |  |  |  |
| AutoFormat [[12]](#12) | 2008 |  | x | x |  |  |
| Tupni [[13]](#13) | 2008 |  | x | x |  |  |
| Boosting [[14]](#14) | 2008 | x |  |  |  | Field(s) |
| ConfigRE [[15]](#15) | 2008 |  | x |  |  |  |
| ReFormat [[16]](#16) | 2009 |  | x | x |  |  |
| Prospex [[17]](#17) | 2009 | x |  | x |  |  |
| Xiao et al. [[18]](#18) | 2009 |  | x |  | x |  |
| Trifilo et al. [[19]](#19) | 2009 | x |  |  | x |  |
| Antunes and Neves [[20]](#20) | 2009 | x |  |  | x |  |
| Dispatcher [[21]](#21) | 2009 |  | x |  |  | C&C malware |
| Fuzzgrind [[22]](#22) | 2009 |  | x |  |  |  |
| REWARDS [[23]](#23) | 2010 |  | x |  |  |  |
| MACE [[24]](#24) | 2010 |  | x |  |  |  |
| ReverX [[25]](#25) | 2011 | x |  |  | x |  |
| Veritas [[26]](#26) | 2011 | x |  |  | x |  |
| Biprominer [[27]](#27) | 2011 | x |  | x | x |  |
| ASAP [[28]](#28) | 2011 | x |  |  |  | Semantics |
| Howard [[29]](#29) | 2011 |  | x |  |  |  |
| ProDecoder [[30]](#30) | 2012 | x |  | x |  |  |
| Zhang et al. [[31]](#31) | 2012 | x |  |  | x |  |
| Netzob [[32]](#32) | 2012 | x | x | x | x |  |
| PRISMA [[33]](#33) | 2012 | x |  |  |  |  |
| ARTISTE [[34]](#34) | 2012 |  | x |  |  |  |
| Wang et al. [[35]](#35) | 2013 | x |  | x |  |  |
| Laroche et al. [[36]](#36) | 2013 | x |  |  | x |  |
| AutoReEngine [[37]](#37) | 2013 | x |  | x | x |  |
| Dispatcher2 [[38]](#38) | 2013 |  | x |  |  | C&C malware |
| ProVeX [[39]](#39) | 2013 | x |  |  |  | Signatures |
| Meng et al. [[40]](#40) | 2014 | x |  |  | x |  |
| AFL [[41]](#41) | 2014 |  | x |  |  |  |
| ProGraph [[42]](#42) | 2015 | x |  | x |  |  |
| FieldHunter [[43]](#43) | 2015 | x |  |  |  | Fields |
| RS Cluster [[44]](#44) | 2015 | x |  |  |  | Grouped-messages |
| UPCSS [[45]](#45) | 2015 | x |  |  |  | Proto-classification |
| ARGOS [[46]](#46) | 2015 |  | x |  |  |  |
| PULSAR [[47]](#47) | 2015 |  |  |  |  |  |
| Cai et al. [[48]](#48) | 2016 | x |  | x |  |  |
| WASp [[49]](#49) | 2016 | x |  | x |  |  |
| PowerShell [[50]](#50) | 2017 | x |  |  |  | Dialogs/scripts |
| ProPrint [[51]](#51) | 2017 | x |  |  |  | Fingerprints |
| ProHacker [[52]](#52) | 2017 | x |  |  |  | Keywords |
| Goo et al. [[53]](#53) | 2019 | x |  | x | x |  |
| Yang et al. [[54]](#54) | 2020 | x |  | x |  |  |
| Sun et al. [[55]](#55) | 2020 |  |  |  |  |  |
| Shim et al. [[56]](#56) | 2020 | x |  | x |  |  |
| IPART [[57]](#57) | 2020 | x |  | x |  |  |

# Input and Output [&uarr;](#table-of-contents)

NetT: input is a network trace (e.g. pcap)<br />
ExeT: input is an execution trace (code/binary at hand)<br />
PF: output is protocol format (describing the syntax)<br />
PFSM: output is protocol finite state machine (describing semantic/sequential logic)<br />

| Name | Year | NetT | ExeT | PF | PFSM | Other Output |
|------|------|------|------|----|------|--------------|
| PIP [[1]](#1) | 2004 | x |  |  |  | Keywords/ fields |
| GAPA [[2]](#2) | 2005 |  | x | x | x |  |
| ScriptGen [[3]](#3) | 2005 | x |  |  |  | Dialogs/scripts |
| RolePlayer [[4]](#4) | 2006 | x |  |  |  | Dialogs/scripts |
| Ma et al. [[5]](#5) | 2006 | x |  |  |  | App-identification |
| FFE/x86 [[6]](#6) | 2006 |  | x |  |  |  |
| Replayer [[7]](#7) | 2006 |  | x |  |  |  |
| Discoverer [[8]](#8) | 2007 | x |  | x |  |  |
| Polyglot [[9]](#9) | 2007 |  | x | x |  |  |
| PEXT [[10]](#10) | 2007 |  | x |  | x |  |
| Rosetta [[11]](#11) | 2007 |  | x |  |  |  |
| AutoFormat [[12]](#12) | 2008 |  | x | x |  |  |
| Tupni [[13]](#13) | 2008 |  | x | x |  |  |
| Boosting [[14]](#14) | 2008 | x |  |  |  | Field(s) |
| ConfigRE [[15]](#15) | 2008 |  | x |  |  |  |
| ReFormat [[16]](#16) | 2009 |  | x | x |  |  |
| Prospex [[17]](#17) | 2009 | x |  | x |  |  |
| Xiao et al. [[18]](#18) | 2009 |  | x |  | x |  |
| Trifilo et al. [[19]](#19) | 2009 | x |  |  | x |  |
| Antunes and Neves [[20]](#20) | 2009 | x |  |  | x |  |
| Dispatcher [[21]](#21) | 2009 |  | x |  |  | C&C malware |
| Fuzzgrind [[22]](#22) | 2009 |  | x |  |  |  |
| REWARDS [[23]](#23) | 2010 |  | x |  |  |  |
| MACE [[24]](#24) | 2010 |  | x |  |  |  |
| ReverX [[25]](#25) | 2011 | x |  |  | x |  |
| Veritas [[26]](#26) | 2011 | x |  |  | x |  |
| Biprominer [[27]](#27) | 2011 | x |  | x | x |  |
| ASAP [[28]](#28) | 2011 | x |  |  |  | Semantics |
| Howard [[29]](#29) | 2011 |  | x |  |  |  |
| ProDecoder [[30]](#30) | 2012 | x |  | x |  |  |
| Zhang et al. [[31]](#31) | 2012 | x |  |  | x |  |
| Netzob [[32]](#32) | 2012 | x | x | x | x |  |
| PRISMA [[33]](#33) | 2012 | x |  |  |  |  |
| ARTISTE [[34]](#34) | 2012 |  | x |  |  |  |
| Wang et al. [[35]](#35) | 2013 | x |  | x |  |  |
| Laroche et al. [[36]](#36) | 2013 | x |  |  | x |  |
| AutoReEngine [[37]](#37) | 2013 | x |  | x | x |  |
| Dispatcher2 [[38]](#38) | 2013 |  | x |  |  | C&C malware |
| ProVeX [[39]](#39) | 2013 | x |  |  |  | Signatures |
| Meng et al. [[40]](#40) | 2014 | x |  |  | x |  |
| AFL [[41]](#41) | 2014 |  | x |  |  |  |
| ProGraph [[42]](#42) | 2015 | x |  | x |  |  |
| FieldHunter [[43]](#43) | 2015 | x |  |  |  | Fields |
| RS Cluster [[44]](#44) | 2015 | x |  |  |  | Grouped-messages |
| UPCSS [[45]](#45) | 2015 | x |  |  |  | Proto-classification |
| ARGOS [[46]](#46) | 2015 |  | x |  |  |  |
| PULSAR [[47]](#47) | 2015 |  |  |  |  |  |
| Cai et al. [[48]](#48) | 2016 | x |  | x |  |  |
| WASp [[49]](#49) | 2016 | x |  | x |  |  |
| PowerShell [[50]](#50) | 2017 | x |  |  |  | Dialogs/scripts |
| ProPrint [[51]](#51) | 2017 | x |  |  |  | Fingerprints |
| ProHacker [[52]](#52) | 2017 | x |  |  |  | Keywords |
| Goo et al. [[53]](#53) | 2019 | x |  | x | x |  |
| Yang et al. [[54]](#54) | 2020 | x |  | x |  |  |
| Sun et al. [[55]](#55) | 2020 |  |  |  |  |  |
| Shim et al. [[56]](#56) | 2020 | x |  | x |  |  |
| IPART [[57]](#57) | 2020 | x |  | x |  |  |

# Tested protocols [&uarr;](#table-of-contents)

| Name | Year | Text-based | Binary-based | Hybrid | Others |
|------|------|------------|--------------|--------|--------|
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
| ReverX [[25]](#25) | 2011 | FTP |  |  |  |
| Veritas [[26]](#26) | 2011 | SMTP | PPLIVE, XUNLEI |  |  |
| Biprominer [[27]](#27) | 2011 |  | XUNLEI, QQLive, SopCast |  |  |
| ASAP [[28]](#28) | 2011 | HTTP, FTP, IRC, TFTP |  |  |  |
| Howard [[29]](#29) | 2011 |  |  |  |  |
| ProDecoder [[30]](#30) | 2012 | SMTP, SIP | SMB |  |  |
| Zhang et al. [[31]](#31) | 2012 | HTTP, SNMP, ISAKMP |  |  |  |
| Netzob [[32]](#32) | 2012 | FTP, Samba | SMB |  | Unknown P2P & VoIP protocol |
| PRISMA [[33]](#33) | 2012 |  |  |  |  |
| ARTISTE [[34]](#34) | 2012 |  |  |  |  |
| Wang et al. [[35]](#35) | 2013 | ICMP | ARP |  |  |
| Laroche et al. [[36]](#36) | 2013 | FTP | DHCP |  |  |
| AutoReEngine [[37]](#37) | 2013 | HTTP, FTP, SMTP, POP3 | DNS, NetBIOS |  |  |
| Dispatcher2 [[38]](#38) | 2013 | HTTP, FTP, ICQ | DNS | SMB |  |
| ProVeX [[39]](#39) | 2013 | HTTP, SMTP, IMAP | DNS, VoIP, XMPP |  | Malware Family Protocols |
| Meng et al. [[40]](#40) | 2014 |  | TCP, ARP |  |  |
| AFL [[41]](#41) | 2014 |  |  |  |  |
| ProGraph [[42]](#42) | 2015 | HTTP | DNS, BitTorrent, WeChat |  |  |
| FieldHunter [[43]](#43) | 2015 | MSNP | DNS |  | SopCast, Ramnit |
| RS Cluster [[44]](#44) | 2015 | FTP, SMTP, POP3, HTTPS | DNS, XunLei, BitTorrent, BitSpirit, QQ, eMule |  | MSSQL, Kugoo, PPTV |
| UPCSS [[45]](#45) | 2015 | HTTP, FTP, SMTP, POP3, IMAP | DNS, SSL, SSH | SMB |  |
| ARGOS [[46]](#46) | 2015 |  |  |  |  |
| PULSAR [[47]](#47) | 2015 |  |  |  |  |
| Cai et al. [[48]](#48) | 2016 | HTTP, SSDP | DNS, BitTorrent, QQ, NetBios |  |  |
| WASp [[49]](#49) | 2016 |  |  |  | Smart plug & PSD systems |
| PowerShell [[50]](#50) | 2017 |  | ARP, OSPF, DHCP, STP |  | CDP/DTP/VTP, HSRP, LLDP, LLMNR, mDNS, NBNS, VRRP |
| ProPrint [[51]](#51) | 2017 |  |  |  |  |
| ProHacker [[52]](#52) | 2017 |  |  |  |  |
| Goo et al. [[53]](#53) | 2019 | HTTP | DNS |  |  |
| Yang et al. [[54]](#54) | 2020 |  | IPv4, TCP |  |  |
| Sun et al. [[55]](#55) | 2020 |  |  |  |  |
| Shim et al. [[56]](#56) | 2020 | FTP | Modbus/TCP, Ethernet/IP |  |  |
| IPART [[57]](#57) | 2020 |  | Modbus, IEC104, Ethernet/IP |  |  |

# Source Code [&uarr;](#table-of-contents)

Most papers do not provide the code used in the research. For the following papers exists (example) code.<br/>
| Name | Year | Source Code |
|------|------|-------------|
| ReverX [[25]](#25) | 2011 | https://github.com/jasantunes/reverx |
| Netzob [[32]](#32) | 2012 | https://github.com/netzob/netzob |

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
W. Cui, J. Kannan, and H. J. Wang, “Discoverer: automatic protocol description generation from network traces,” in Proceedings of the USENIX Security Symposium, 2007. 
#### [9]
J. Caballero, H. Yin, Z. Liang, and D. Song, “Polyglot: automatic extraction of protocol message format using dynamic binary analysis,” in Proceedings of the 14th ACM Conference on Computer and Communications Security (CCS ’07), pp. 317–329, ACM, November 2007.
#### [10]
M. Shevertalov and S. Mancoridis, “A reverse engineering tool for extracting protocols of networked applications,” in Proceedings of the 14th Working Conference on Reverse Engineering (WCRE ’07), pp. 229–238, October 2007.
#### [11]
Caballero, J., Song, D.: Rosetta: Extracting Protocol Semantics Using Binary Analysis with Applications to Protocol Replay and NAT Rewriting. Technical Report CMU-CyLab-07-014, Carnegie Mellon University, Pittsburgh (2007)
#### [12]
Z. Lin, X. Jiang, D. Xu, and X. Zhang, “Automatic protocol format reverse engineering through context-aware monitored execution,” in Proceedings of the 15th Symposium on Network and  Distributed System Security (NDSS ’08), February 2008.
#### [13]
W. Cui, M. Peinado, K. Chen, H. J. Wang, and L. Irun-Briz, “Tupni: automatic reverse engineering of input formats,” in Proceedings of the 15th ACM Conference on Computer and Communications Security (CCS ’08), pp. 391–402, ACM, Alexandria, Va, USA, October 2008.
#### [14]
K. Gopalratnam, S. Basu, J. Dunagan, and H. J. Wang, “Automatically extracting fields from unknown network protocols,” in Proceedings of the 15th Symposium on Network and Distributed System Security (NDSS ’08), 2008. [PDF](http://www.nicemice.net/helen/papers/sysml-Gopalratnam.pdf)
#### [15]
Wang, R., Wang, X., Zhang, K., Li, Z.: Towards automatic reverse engineering of software security configurations. In: Proceedings of the 15th ACM Conference on Computer and Communications Security, CCS ’08, pp. 245–256. ACM, Limerick (2008). doi:10.1145/1455770.1455802
#### [16]
Z. Wang, X. Jiang, W. Cui, X. Wang, and M. Grace, “ReFormat: automatic reverse engineering of encrypted messages,” in Computer Security—ESORICS 2009. ESORICS 2009, M. Backes and P. Ning, Eds., vol. 5789 of Lecture Notes in Computer Science, pp. 200–215, Springer, Berlin, Germany, 2009.
#### [17]
P. M. Comparetti, G. Wondracek, C. Kruegel, and E. Kirda, “Prospex: protocol specification extraction,” in Proceedings of the 30th IEEE Symposium on Security and Privacy, pp. 110–125, Berkeley, Calif, USA, May 2009.
#### [18]
M.-M. Xiao, S.-Z. Yu, and Y. Wang, “Automatic network protocol automaton extraction,” in Proceedings of the 3rd International Conference on Network and System Security (NSS ’09), pp. 336–343, October 2009.
#### [19]
A. Trifilo, S. Burschka, and E. Biersack, “Traffic to protocol reverse engineering,” in Proceedings of the IEEE Symposium on Computational Intelligence for Security and Defense Applications, pp. 1–8, July 2009.
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
J. Antunes, N. Neves, and P. Verissimo, “Reverse engineering of protocols from network traces,” in Proceedings of the 18th Working Conference on Reverse Engineering (WCRE ’11), pp. 169–178, October 2011.
#### [26]
Y. Wang, Z. Zhang, D. D. Yao, B. Qu, and L. Guo, “Inferring protocol state machine from network traces: a probabilistic approach,” in Proceedings of the 9th Applied Cryptography and Network Security International Conference (ACNS ’11), pp. 1–18, 2011.
#### [27]
Y. Wang, X. Li, J. Meng, Y. Zhao, Z. Zhang, and L. Guo, “Biprominer: automatic mining of binary protocol features,” in Proceedings of the 12th International Conference on Parallel and Distributed Computing, Applications and Technologies (PDCAT ’11), pp. 179–184, October 2011.
#### [28]
T. Krueger, N. Krmer, and K. Rieck, “Asap: automatic semantics-aware analysis of network payloads,” in Proceedings of the ECML/PKDD, 2011. [PDF](https://oar.tib.eu/jspui/bitstream/123456789/2288/1/664831966.pdf)
#### [29]
Slowinska, A., Stancescu, T., Bos, H.: Howard: a dynamic excavator for reverse engineering data structures. In: Proceedings of the 18th Annual Network and Distributed System Security Symposium (NDSS). Internet Society, San Diego (2011)
#### [30]
Y. Wang, X. Yun, M. Z. Shafiq et al., “A semantics aware approach to automated reverse engineering unknown protocols,” in Proceedings of the 20th IEEE International Conference on Network Protocols (ICNP ’12), pp. 1–10, IEEE, Austin, Tex, USA, November 2012.
#### [31]
Z. Zhang, Q.-Y. Wen, and W. Tang, “Mining protocol state machines by interactive grammar inference,” in Proceedings of the 2012 3rd International Conference on Digital Manufacturing and Automation (ICDMA ’12), pp. 524–527, August 2012.
#### [32]
G. Bossert, F. Guihéry, and G. Hiet, “Towards automated protocol reverse engineering using semantic information,” in Proceedings of the 9th ACM Symposium on Information, Computer and Communications Security, Kyoto, Japan, June 2014.
G. Bossert and F. Guihéry, “Reverse and simulate your enemy botnet C&C,” in Proceedings of the Mapping a P2P Botnet with Netzob, Black Hat 2012, Abu Dhabi, UAE, December 2012. [PDF](https://www.amossys.fr/upload/publication.pdf)
#### [33]
Krueger, T., Gascon, H., Krmer, N., Rieck, K.: Learning stateful models for network honeypots. In: Proceedings of the 5th ACM Workshop on Security and Artificial Intelligence, AISec ’12, pp. 37–48. ACM, New York, NY (2012). doi:10.1145/2381896.2381904
#### [34]
Caballero, J., Grieco, G., Marron, M., Lin, Z., Urbina, D.: ARTISTE: Automatic Generation of Hybrid Data Structure Signatures from Binary Code Executions. Technical Report TR-IMDEA-SW-2012-001, IMDEA Software Institute, Madrid (2012)
#### [35]
Y. Wang, N. Zhang, Y.-M. Wu, B.-B. Su, and Y.-J. Liao, “Protocol formats reverse engineering based on association rules in wireless environment,” in Proceedings of the 12th IEEE International Conference on Trust, Security and Privacy in Computing and Communications (TrustCom ’13), pp. 134–141, Melbourne, Australia, July 2013.
#### [36]
P. Laroche, A. Burrows, and A. N. Zincir-Heywood, “How far an evolutionary approach can go for protocol state analysis and discovery,” in Proceedings of the IEEE Congress on Evolutionary Computation (CEC ’13), pp. 3228–3235, June 2013.
#### [37]
J.-Z. Luo and S.-Z. Yu, “Position-based automatic reverse engineering of network protocols,” Journal of Network and Computer Applications, vol. 36, no. 3, pp. 1070–1077, 2013.
#### [38]
J. Caballero and D. Song, “Automatic protocol reverse-engineering: message format extraction and field semantics inference,” Computer Networks, vol. 57, no. 2, pp. 451–474, 2013. [PDF](http://www.academia.edu/download/47267446/j.comnet.2012.08.00320160715-7025-1uns1ji.pdf)
#### [39]
C. Rossow and C. J. Dietrich, “PROVEX: detecting botnets with encrypted command and control channels,” in Detection of Intrusions and Malware, and Vulnerability Assessment, Springer, 2013. [PDF](https://chrisdietri.ch/files/provex-dimva2013.pdf)
#### [40]
F. Meng, Y. Liu, C. Zhang, T. Li, and Y. Yue, “Inferring protocol state machine for binary communication protocol,” in Proceedings of the IEEE Workshop on Advanced Research and Technology in Industry Applications (WARTIA ’14), pp. 870–874, September 2014.
#### [41]
Zalewski, M.: American Fuzzy Loop. http://lcamtuf.coredump.cx/afl/technical_details.txt
#### [42]
Q. Huang, P. P. C. Lee, and Z. Zhang, “Exploiting intrapacket dependency for fine-grained protocol format inference,” in Proceedings of the 14th IFIP Networking Conference (NETWORKING ’15), Toulouse, France, May 2015.
#### [43]
I. Bermudez, A. Tongaonkar, M. Iliofotou, M. Mellia, and M. M. Munafo, “Automatic protocol field inference for deeper protocol understanding,” in Proceedings of the 14th IFIP Networking Conference (Networking ’15), pp. 1–9, May 2015. [PDF](http://dl.ifip.org/db/conf/networking/networking2015/1570062733.pdf)
#### [44]
J.-Z. Luo, S.-Z. Yu, and J. Cai, “Capturing uncertainty information and categorical characteristics for network payload grouping in protocol reverse engineering,” Mathematical Problems in Engineering, vol. 2015, Article ID 962974, 9 pages, 2015.
#### [45]
R. Lin, O. Li, Q. Li, and Y. Liu, “Unknown network protocol classification method based on semi supervised learning,” in Proceedings of the IEEE International Conference on Computer and Communications (ICCC ’15), pp. 300–308, Chengdu, China, October 2015.
#### [46]
Zeng, J., Lin, Z.: Towards automatic inference of kernel object semantics from binary code. In: 18th International Symposium, RAID 2015, vol. 9404, pp. 538–561. Springer, Kyoto (2015). doi:10.1007/978-3-319-26362-5
#### [47]
[1]H. Gascon, C. Wressnegger, F. Yamaguchi, D. Arp, and K. Rieck, “Pulsar: Stateful Black-Box Fuzzing of Proprietary Network Protocols,” in Security and Privacy in Communication Networks, vol. 164, B. Thuraisingham, X. Wang, and V. Yegneswaran, Eds. Cham: Springer International Publishing, 2015, pp. 330–347.  [PDF](http://user.cs.uni-goettingen.de/~krieck/docs/2015-securecomm.pdf)
#### [48]
J. Cai, J. Luo, and F. Lei, “Analyzing network protocols of application layer using hidden Semi-Markov model,” Mathematical Problems in Engineering, vol. 2016, Article ID 9161723, 14 pages, 2016.
#### [49]
K. Choi, Y. Son, J. Noh, H. Shin, J. Choi, and Y. Kim, “Dissecting customized protocols: automatic analysis for customized protocols based on IEEE 802.15.4,” in Proceedings of the 9th ACM Conference on Security and Privacy in Wireless and Mobile Networks, pp. 183–193, Darmstadt, Germany, July 2016.
#### [50]
D. R. Fletcher Jr., Identifying Vulnerable Network Protocols with PowerShell, SANS Institute Reading Room site, 2017.
#### [51]
Y. Wang, X. Yun, Y. Zhang, L. Chen, and G. Wu, “A nonparametric approach to the automated protocol fingerprint inference,” Journal of Network and Computer Applications, vol. 99, pp. 1–9, 2017.
#### [52]
Y. Wang, X. Yun, Y. Zhang, L. Chen, and T. Zang, “Rethinking robust and accurate application protocol identification,” Computer Networks, vol. 129, pp. 64–78, 2017.
#### [53]
[1]Y.-H. Goo, K.-S. Shim, M.-S. Lee, and M.-S. Kim, “Protocol Specification Extraction Based on Contiguous Sequential Pattern Algorithm,” IEEE Access, vol. 7, pp. 36057–36074, 2019, doi: 10.1109/ACCESS.2019.2905353.  [PDF](https://ieeexplore.ieee.org/iel7/6287639/6514899/08667834.pdf)
#### [54]
[1]C. Yang, C. Fu, Y. Qian, Y. Hong, G. Feng, and L. Han, “Deep Learning-Based Reverse Method of Binary Protocol,” in Security and Privacy in Digital Economy, vol. 1268, S. Yu, P. Mueller, and J. Qian, Eds. Singapore: Springer Singapore, 2020, pp. 606–624. 
#### [55]
[1]F. Sun, S. Wang, C. Zhang, and H. Zhang, “Clustering of unknown protocol messages based on format comparison,” Computer Networks, vol. 179, p. 107296, Oct. 2020, doi: 10.1016/j.comnet.2020.107296. 
#### [56]
[1]K. Shim, Y. Goo, M. Lee, and M. Kim, “Clustering method in protocol reverse engineering for industrial protocols,” International Journal of Network Management, Jun. 2020, doi: 10.1002/nem.2126.  [PDF](https://nmlab.korea.ac.kr/publication/published.papers/2020/2020.06_Clustering_method_for_ICS-APRE-IJNM.pdf)
#### [57]
[1]X. Wang, K. Lv, and B. Li, “IPART: an automatic protocol reverse engineering tool based on global voting expert for industrial protocols,” International Journal of Parallel, Emergent and Distributed Systems, vol. 35, no. 3, pp. 376–395, May 2020, doi: 10.1080/17445760.2019.1655740. 
