# Waning of immunity 

Teams are encouraged to incorporate the waning of immunity conferred by both la-mAbs and MV into their models. To facilitate this, we provide the file [waning_curves.csv](./waning_curves.csv), which contains immunity waning data derived from [Hodgson et al. (2024)](https://www.thelancet.com/journals/lanepe/article/PIIS2666-7762(23)00248-X/fulltext). Specifically, the file includes the following columns:

- ```days```: days post-immunisation
- ```la_mabs_waning```: waning of la-mAbs immunity. This is expressed as the percentage of the initial la-mAbs protection at day 0 (i.e., 50% indicates that the la-mAbs protection is reduced to 50% of the initial level)
- ```MV_neonates_waning```: waning of MV immunity for neonates, with the same interpretation as ```la_mabs_waning```.
- ```MV_mothers_waning```: waning of MV immunity for mothers, with the same interpretation as ```la_mabs_waning```.
- ```la_mabs_severe_waning```: waning of la-mAbs protection against severe RSV disease, with the same interpretation as ```la_mabs_waning```.
- ```MV_neonates_severe_waning```: waning of MV protection against severe RSV disease for neonates, with the same interpretation as ```la_mabs_waning```.
- ```MV_mothers_severe_waning```: waning of MV protection against severe RSV disease for mothers, with the same interpretation as ```la_mabs_waning```.

These data were extracted from Figure 2 of [Hodgson et al. (2024)](https://www.thelancet.com/journals/lanepe/article/PIIS2666-7762(23)00248-X/fulltext), specifically the mean values of the waning curves. The figure shows the proportion of individuals protected over time, with the x-axis representing days post-immunisation and the y-axis the corresponding protection levels. The authors employed a Bayesian framework to estimate the efficacy and waning of protection for each product using clinical trial data for MV and la-mAB. They assumed vaccine-induced immunity wanes according to an Erlang distribution with shape parameter 3. The values that we report here are the mean values of these waning curves divided by the initial protection level and expressed as a percentage.

We refer teams also to [Xu et al., 2025](https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2831181) (Figure 3) for additional data on the waning of immunity conferred by la-mAbs against various clinical outcomes of RSV.