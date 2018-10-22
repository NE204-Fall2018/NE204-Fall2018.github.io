title: Instruments
page-order: 06
date: 2018-08-16
modified: 2018-08-16

## Available Instrumentation

Due to time-intensive nature of the laboratory investigations and the large
enrollment, not every student will be participating in *every* listed lab.
Instead, all students will conduct lab experiments focusing on DSP with 
coaxial HPGe detectors, then will be responsible for selecting from the
[list of potential experiments]({filename}/labs/writeups.md) for the third lab
report.

In addition, the final project for the course requires students to propose an
instrumentation-focused study.
Below is an (incomplete) list of instruments and measurement systems that are
available for NE 204.
Available relevant information is included for some systems - updates will 
continue as more information becomes available.
Some of the instruments are a good fit for one or more of the experiment
writeups, while others are not (yet) explicitly tied to any particular
experiment.
Please consider these instruments for the rotating labs and final project
proposals.

### LaBr
![LaBr]({filename}/downloads/LaBr.png)   
**Description**: 2 in. x 2 in. LaBr scintillator with 3 in. Hamamatsu
[r6233-100](https://www.hamamatsu.com/eu/en/product/type/R6233/index.html)  
 - Operating Voltage: +540V  
 - Ener. Res. @ 662 keV: 2.6% (from manufacturer)  
**Location**: Etcheverry Hall (1110B or 1140)  
**Readout**: Analog PMT base + SIS | Analog PMT base + NIM | 
             [Digibase](https://www.ortec-online.com/products/electronics/photomultiplier-tube-bases/digibase-e) |
             SIS33XX   
**Related Experiments**: [Lab 3]({filename}/downloads/lab3_writeup.pdf), 
                         Time resolution (cf. NE104 Lab 6)  
**Status**: <font color="green">Working as of 10/2/2018</font>  
**Additional Documentation**: None  

### CCI-2 (VCI)
![CCI2]({filename}/downloads/CCI2.png)    
**Description**: 2x Double-sided strip HPGe detector  
 - 2 planar detectors, each 15.1 mm thick, segmented orthogonal-strip electrodes  
 - 152 Strips, 2mm pitch, 0.25mm gap, 5mm guard ring  
 - Operating Voltage: +800V  
 - Ener. Res. @ 662 keV: 0.19 - 0.5% (depending on strip)  
**Location**: 1140 Etcheverry Hall  
**Readout**: SIS3302/3150  
**Related Experiments**: [Lab 5]({filename}/downloads/lab5_writeup.pdf), 
                         [Lab 6]({filename}/downloads/lab6_writeup.pdf),
                         [Lab 8]({filename}/downloads/lab8_writeup.pdf)  
**Status**: <font color="orange">Hopefully available by 10/18/18</font>  
**Additional Documentation**: [CCI2 TechReport 1](https://bcourses.berkeley.edu/courses/1474357/files/?preview=73814889),
                              [CCI2 TechReport 2](https://bcourses.berkeley.edu/courses/1474357/files/?preview=73814890)   

### UCBGe2\_2008 (re-fabbed in 2011)
**Description**: Double-sided strip HPGe detector  
 - 11 mm thick, segmented orthogonal-strip electrodes  
 - 76 Strips (38 per side), 2mm pitch, 0.25mm gap, 5mm guard ring  
 - Operating Voltage: +1000V  
 - Ener. Res. @ 662 keV: 0.19 - 0.5% (depending on strip)  
**Location**: LBNL SDL (70A)  
**Readout**: SIS3302/3150  
**Related Experiments**: [Lab 5]({filename}/downloads/lab5_writeup.pdf), 
                         [Lab 6]({filename}/downloads/lab6_writeup.pdf),
                         [Lab 8]({filename}/downloads/lab8_writeup.pdf)  
**Status**: <font color="red">Unavailable for Fall 2018</font>    
**Additional Documentation**: [UCB2008 Ge2 Refabrication Report (2011)](https://bcourses.berkeley.edu/courses/1474357/files/?preview=73815778)

### UCBGe3\_2011
**Description**: Double-sided strip HPGe detector  
 - 15.1 mm thick, segmented orthogonal-strip electrodes  
 - 152 Strips, 2mm pitch, 0.25mm gap, 5mm guard ring  
 - Operating Voltage: <font color="orange">See docs</font>  
 - Ener. Res. @ 662 keV: <font color="orange">See docs</font>  
**Location**: LBNL SDL (70A)
**Readout**: SIS3302/3150  
**Related Experiments**: [Lab 5]({filename}/downloads/lab5_writeup.pdf), 
                         [Lab 6]({filename}/downloads/lab6_writeup.pdf)   
**Status**: <font color="orange">**Only half instrumented**</font>  
**Additional Documentation**: None  

### Large Area Imager
![LAI]({filename}/downloads/LAI.png)   
**Description**: 10x10 NaI(Tl) Coded Aperture Imager  
 - 10x10 array of NaI(Tl) detectors w/ PMTs  
 - 4x4x4 in. NaI(Tl) crystals  
 - Coded aperture array, random configuration, 1 in. thick Pb elements   
 - Operating Voltage: <1200V (varies by channel)   
 - Ener. Res. @ 662 keV: ~9% (varies by channel)   
**Location**: 1140 Etcheverry Hall   
**Readout**: SIS3302/3150   
**Related Experiments**:  [Lab 8 (CA)]({filename}/downloads/lab8_writeup.pdf)    
**Status**: <font color="green">Available, 96/100 channels working</font>  
**Additional Documentation**: None  

### Liquid Scintillation Detector (LSD) Scatter Camera
**Description**: 2-plane, 24 element kinematic neutron imager
 - 24 detectors (12 per plane)  
 - 2 in. x 2 in. EJ309 (xylene-based) liquid scintillators  
 - Operating Voltage: ~ -1350V (varies by channel)   
 - Ener. Res. @ 662 keV: N/A  
**Location**: 1140 Etcheverry Hall, 1140B   
**Readout**: SIS3320 | SIS3316   
**Related Experiments**:  [Lab 4]({filename}/downloads/lab4_writeup.pdf)
                          [Lab 9]({filename}/downloads/lab9_writeup.pdf)   
**Status**: <font color="orange">Available, readout requires setup</font>  
**Additional Documentation**: None  

### Pixelated CZT
![CZT]({filename}/downloads/PixelatedCZT.png)   
**Description**: 10 mm3 CZT w/ 3x3 pixellated anode   
 - 1 cm3 crystal, 3x3 pixellated anode + guard ring (see docs)  
 - Operating Voltage: ~ -1000V (see docs)  
 - Ener. Res. @ 662 keV: see docs   
**Location**: 1140 Etcheverry Hall, modular room   
**Readout**: SIS3302/3150   
**Related Experiments**:  [Lab 7]({filename}/downloads/lab7_writeup.pdf)  
**Status**: <font color="green">2 Detectors Available</font>  
**Additional Documentation**: [UCBCZT1](https://bcourses.berkeley.edu/courses/1474357/files/?preview=73815805),
                              [UCBCZT2](https://bcourses.berkeley.edu/courses/1474357/files/?preview=73815806)   

### PSD Plastics
**Description**: 1 in. or 2 in. Plastic Scint. w/ PSD  
 - PSD-capable plastic scintillators from Dr. Natalia Zaitseva, LLNL   
**Location**: 1140 Etcheverry Hall, modular room  
**Readout**: SIS3302/3150   
**Related Experiments**:  [Lab 4 (PSD)]({filename}/downloads/lab4_writeup.pdf)    
**Status**: <font color="red">Un-instrumented, PMTs/bases on order</font>  
**Additional Documentation**: None  

### CLYC Detector
![CLYC]({filename}/downloads/CLYC.png)   
**Description**: 2x2 in. CLYC Detector  
 - PSD-capable detector for n/gamma discrimination   
 - Moderate (~4%) Energy resolution  
**Location**: 1140 Etcheverry Hall   
**Readout**: [Bridgeport Systems eMorpho](https://www.bridgeportinstruments.com/products/usb_base/usb_base.html)  
**Related Experiments**:  [Lab 4 (PSD)]({filename}/downloads/lab4_writeup.pdf)    
**Status**: <font color="green">Integrated eMorpho PMT/Base Operational w/ working software</font>    
**Additional Documentation**: [CLYC](http://rmdinc.com/wp-content/uploads/2016/06/CLYC-Properties-5-10-16.pdf)   

### LSO Array & Coded Aperture
![LSO]({filename}/downloads/LSO.png)   
**Description**: 16 LSO Modules, 4 PMTs per module   
 - Subset of array formerly used for a PET system   
 - Excellent time response (O(100 ps))   
 - Includes 2D coded-aperture mask for high-energy gamma-ray imaging   
**Location**: 1140 Etcheverry Hall, modular room   
**Readout**: SIS3316 (Ethernet or SIS3150 readout)   
**Related Experiments**:  [Lab 3 (Timing)]({filename}/downloads/lab3_writeup.pdf),
                          [Lab 8 (CA)]({filename}/downloads/lab8_writeup.pdf)    
**Status**: <font color="orange">3150 for off-line readout, 3316 real-time readout under development</font>    
**Additional Documentation**: None

### Plastic/Lead System

### NaI Bars

### 100%ers

