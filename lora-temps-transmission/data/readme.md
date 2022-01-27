# Data sets location
This directory contains three another ones related to the data sets and called **raw**, **processed**, **cleaned**. A description of each one is given below. 

## Raw directory
This directory contains original and immutable data sets. Do not edit raw data, especially with Excel, open files only in read only mode. Each data file is related to an experiment with a specific spreading factor, coding rate and bandwidth. All data files have the following structure :

- TIteration : time after loop begins (*see source code in the reference directory*)
- TBlock : time after socket creation (*see source code in the reference directory*)
- TMessGen : time after generated data (*see source code in the reference directory*)
- TMessSend : time after sending data (*see source code in the reference directory*)
- TDisplay : time when display info (*see source code in the reference directory*)
- TOA : theoretical time on air (time to transmit data)
- Essai : number of retransmission
- TxPower : power of the transmitted signal
- SF : spreading factor
- Bandwith : bandwidth
- CodingRate : coding rate
- Taille : size of sending data

## Processed directory
This directory contains intermediate transformed data sets. This working directory could contain multiple data sets.

## Cleaned directory
This directory contains canonical data sets could be used for publication. These data sets would be used for the analysis.
