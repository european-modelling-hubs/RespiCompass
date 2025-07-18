# Waning of immunity 

Teams are encouraged to incorporate the waning of immunity conferred by both la-mAbs and MV into their models. Note that the IE values listed in the shared assumptions of this round (see [scenario round specifications](../../round1_2526_rsv.md)) refer to 
a meta-analysis considering 8 studies with an observation period between 4 and 8 months in the case of la-mAbs [1], while the IE of MV is estimated considering newborns from birth to age 3 month [2].

To facilitate the inclusion of waning of immunity in the models, we provide the file [waning_curves.csv](./waning_curves.csv), which contains immunity waning data derived from Ref. [3]. Specifically, the file includes the following columns:

- ```days_post_intervention```: days post-immunisation
- ```la_mAbs```: waning of la-mAbs immunity. This is expressed as the percentage of the initial la-mAbs protection at day 0 (i.e., 50.0 indicates that the la-mAbs protection is reduced to 50% of the initial level)
- ```mv_neonates```: waning of MV immunity for neonates, with the same interpretation as ```la_mAbs```.
- ```mv_pregnant```: waning of MV immunity for pregnant individuals, with the same interpretation as ```la_mAbs```.
- ```la_mAbs_severe```: waning of la-mAbs protection against severe RSV disease, with the same interpretation as ```la_mAbs```.
- ```mv_neonates_severe```: waning of MV protection against severe RSV disease for neonates, with the same interpretation as ```la_mAbs```.
- ```mv_pregnant_severe```: waning of MV protection against severe RSV disease for pregnant individuals, with the same interpretation as ```la_mAbs```.

These data were extracted from Figure 2 of Ref. [3], specifically the mean values of the waning curves. The figure shows the proportion of individuals protected over time, with the x-axis representing days post-immunisation and the y-axis the corresponding protection levels. The authors employed a Bayesian framework to estimate the efficacy and waning of protection using clinical trial data for MV and la-mAB. They assumed vaccine-induced immunity wanes according to an Erlang distribution with shape parameter 3. The values that we report here are the mean values of these waning curves divided by the initial protection level and expressed as a percentage.

In Ref. [3], efficacy against milder and more severe outcomes is modelled considering efficacy against the following outcomes:

- Milder outcomes:
    - MV (neonates): infection, symptomatic cases, GP consultations
    - MV (pregnant women): infection, symptomatic cases, GP consultations, A&E; 
    - la-mAB: infection, symptomatic cases, GP consultations, A&E and hospitalisation. 
- Severe outcomes:
    - MV (neonates): severe lower respiratory tract infection (LRTI)
    - MV (pregnant women): severe lower respiratory tract infection (LRTI)
    - la-mAB: very severe LRTI


We refer teams also to Ref. [4] (Figure 3) for additional data on the waning of immunity conferred by la-mAbs against various clinical outcomes of RSV.


# References 
1. Xiao Li, Roberfroid Dominique, Bilcke Joke, Castanares-Zapatero Diego, de Meester Christophe, Mao Zhuxin, Thiry Nancy, Willem Lander, Beutels Philippe. Cost-effectiveness of new preventive options against RSV infections in Belgian infants. Health Technology Assessment (HTA). Brussels. Belgian Health Care Knowledge Centre (KCE). 2025. KCE Reports 402C. DOI: 10.57598/R402C. Available at: https://kce.fgov.be/en/publications/all-reports/cost-effectiveness-of-new-preventive-options-against-rsv-infections-in-belgian-infants
2. Marc GP, Vizzotti C, Fell DB, Di Nunzio L, Olszevicki S, Mankiewicz SW, Braem V, Rearte R, Atwell JE, Bianchi A, Fuentes N. Real-world effectiveness of RSVpreF vaccination during pregnancy against RSV-associated lower respiratory tract disease leading to hospitalisation in infants during the 2024 RSV season in Argentina (BERNI study): a multicentre, retrospective, test-negative, case–control study. The Lancet Infectious Diseases. 2025 May 5. Available at: https://www.thelancet.com/journals/laninf/article/PIIS1473-3099(25)00156-2/abstract
3. Hodgson D, Wilkins N, van Leeuwen E, Watson CH, Crofts J, Flasche S, Jit M, Atkins KE. Protecting infants against RSV disease: an impact and cost-effectiveness comparison of long-acting monoclonal antibodies and maternal vaccination. The Lancet Regional Health–Europe. 2024 Mar 1;38. Available at: https://www.thelancet.com/journals/lanepe/article/PIIS2666-7762(23)00248-X/fulltext
4. Xu H, Aparicio C, Wats A, Araujo BL, Pitzer VE, Warren JL, Shapiro ED, Niccolai LM, Weinberger DM, Oliveira CR. Estimated effectiveness of nirsevimab against respiratory syncytial virus. JAMA network open. 2025 Mar 3;8(3):e250380-. Available at: https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2831181