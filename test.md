# Carbon Relevant Paper Links

A list of carbon relevant paper links. If you have any comment, please create an [issue](https://github.com/zhaoyujieseberena/Carbon/issues) or [pull request](https://github.com/zhaoyujieseberena/Carbon/pulls).

## Contents
- [Exisiting metrics](##Exisiting metrics)
- [Useful Links](##Useful Links)
  - [Estimation parameters](###Estimation parameters)
  - [Tools](###Tools)
- [Papers](##papers)
  - [Review](###Review)
  - [Optimation](###Optimation)
  - [Calculation](###Calculation)
  - [Standardization](###Standardization)

## Legend

| Target Problem                                                                    | Computer system stack                          | Hardware system                    | Carbon life cycle stage(s)               |
| --------------------------------------------------------------------------------- | ---------------------------------------------- | ---------------------------------- | ---------------------------------------- |
| [![1](images/square1.svg)](Classification/Target_Problem.md#Optimation)Optimation | ![1](images/square5.svg) Application           | ![1](images/square.svg)Datacenter  | ![1](images/square6.svg)Manufacturing    |
| ![1](images/star1.svg)Modeling                                                    | ![1](images/star5.svg)OS                       | ![1](images/star.svg)Edge          | ![1](images/star6.svg)Operation          |
| ![1](images/stop-circle1.svg)Standardization                                      | ![1](images/stop-circle5.svg)Microarchitecture | ![1](images/stop-circle.svg)Mobile | ![1](images/stop-circle6.svg)End-of-life |
| ![1](images/target1.svg)Review                                                    | ![1](images/target5.svg)Infrastructure         | ![1](images/target.svg)TinyML      |                                          |
## Metrics
| Metric | Computer system stack | Hardware system | Carbon life cycle stage(s) | 
| :---: | :------: | :------: | :--------: | 
|PUE|[![1](images/target5.svg)]()|[![1](images/square.svg)]()|[![1](images/star6.svg)]()|
|GPUE|[![1](images/target5.svg)]()|[![1](images/square.svg)]()|[![1](images/star6.svg)]()|
|CUE|[![1](images/target5.svg)]()|[![1](images/square.svg)]()|[![1](images/star6.svg)]()|
|CCI|[![1](images/target5.svg)]()|[![1](images/square.svg)]()|[![1](images/star6.svg)]()|
|SCI|[![1](images/square5.svg)]()|[![1](images/square.svg)]()[![1](images/star.svg)]()[![1](images/stop-circle.svg)]()|[![1](images/square6.svg)]()[![1](images/star6.svg)]()|
|CDP/CEP|[![1](images/stop-circle5.svg)]()|[![1](images/square.svg)]()[![1](images/star.svg)]()[![1](images/stop-circle.svg)]()|[![1](images/square6.svg)]()[![1](images/star6.svg)]()|
|tCDP/tCEP|[![1](images/stop-circle5.svg)]()|[![1](images/square.svg)]()[![1](images/star.svg)]()[![1](images/stop-circle.svg)]()|[![1](images/square6.svg)]()[![1](images/star6.svg)]()|
|JSC|[![1](images/square5.svg)]()|[![1](images/square.svg)]()[![1](images/star.svg)]()[![1](images/stop-circle.svg)]()|[![1](images/square6.svg)]()[![1](images/star6.svg)]()|
|ASC|[![1](images/square5.svg)]()|[![1](images/square.svg)]()[![1](images/star.svg)]()[![1](images/stop-circle.svg)]()|[![1](images/square6.svg)]()[![1](images/star6.svg)]()|

| Metric | Description | Link |  
| :---: | :--------: | :----: | 
|PUE|Power Usage Effectiveness of a dedicated data center| [[Paper]](https://www.thegreengrid.org/en/resources/library-and-tools/20-pue%3A-a-comprehensive-examination-of-the-metric)|
|GPUE|Green Power Usage Effectivenes| [[Paper]](https://ieeexplore.ieee.org/document/8701895)|
|CUE|Carbon Usage Effectiveness| [[Paper]](https://airatwork.com/wp-content/uploads/The-Green-Grid-White-Paper-32-CUE-Usage-Guidelines.pdf)|
|CCI|Computational Carbon Intensity| [[Paper]](https://arxiv.org/abs/2110.06870)|
|SCI|Software Carbon Intensity| [[Paper]](https://github.com/Green-Software-Foundation/sci/blob/main/Software_Carbon_Intensity/Software_Carbon_Intensity_Specification.md)|
|CDP/CEP|Product of Carbon Delay/Energy | [[Paper]](https://ieeexplore.ieee.org/document/10122998)|
|tCDP/tCEP|Product of total CO2 and total application execution time| [[Paper]](https://arxiv.org/abs/2305.01831)|
|JSC|Job Sustainability Costs| [[Paper]](https://par.nsf.gov/servlets/purl/10353075)|
|ASC|Amortized Sustainability Costs| [[Paper]](https://par.nsf.gov/servlets/purl/10353075)|

### Tools

| Name         | Link                                             | Description                                                                                                                                                   |
| ------------ | ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Codecarbon   | https://github.com/mlco2/codecarbon              | Track emissions from Compute and recommend ways to reduce their impact on the environment.                                                                    |
| Hyrax system | https://www.hyraxsystems.com/                    | The _Hyrax System_ works by absorbing the free latent energy in the surrounding environment and atmosphere, and converting it into hot water for DHW or space |
| TinyML       | https://github.com/harvard-edge/TinyML-Footprint | A tool to calculate embodied and operation carbon of TinyML in different hardware configuration.                                                              |
| Greenchip    | https://github.com/Pitt-JonesLab/Greenchip       | A tool designed to compare energy and emission costs between computer chips                                                                                   |
| 3D-Carbon    | https://anonymous.4open.science/r/3D-Carbon-9D5B | A analytical tool to calculate embodied and operation carbon of 3D/2.5D ICs.                                                                                  |
| ACT          | https://github.com/facebookresearch/ACT          | An analytical, architectural carbon model to estimate operational and embodied carbon.                                                                        |
| McPAT        | https://github.com/HewlettPackard/mcpat          | Architectural integrated power, area, and timing modeling framework, focuses on power and area modeling, with a target clock rate as a design constraint.     |

### Estimation parameters

| Parameters           | Link                                                                                                                                                                                                                                                                                                                                                    |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| MCU embodied carbon  | https://www.st.com/content/st_com/en/about/sustainability/sustainable-technology.html                                                                                                                                                                                                                                                                   |
| Embodied carbon      | https://github.com/Boavizta/environmental-footprint-data/blob/main/boavizta-data-us.csv                                                                                                                                                                                                                                                                 |
| Carbon density       | a. https://www.eea.europa.eu/data-and-maps/data/co2-intensity-of-electricity-generation b. https://www.eea.europa.eu/data-and-maps/indicators/average-co2-emissions-from-motor-vehicles/assessment-1                                                                                                                                                    |
| IC's Embodied carbon | DTCO including Sustainability: Power-Performance-Area-CostEnvironmental score (PPACE) Analysis for Logic Technologies                                                                                                                                                                                                                                   |
| ReRAM's embodied     | a. How Low Can You Go?An Inside Look at Weebit ReRAM Power Consumption https://www.weebit-nano.com/how-low-can-you-goan-inside-look-at-weebit-reram-power-consumption/ b.Weebit ReRAM:NVM that’s better for the planet https://www.weebit-nano.com/weebit-nano-rram-reram-ip-nvm-for-semiconductors-green-materials-eco-friendly-technology-production/ |
## Papers
| Metric | Target problem | Computer system stack | Hardware system | Carbon life cycle stage(s) | 
| :---: | :----: | :------: | :------: | :--------: | 
|[1](#paper1)|[![1](images/star1.svg)]()|[![1](images/square5.svg)]()[![1](images/target5.svg)]()|[![1](images/square.svg)]()[![1](images/star.svg)]()|[![1](images/square6.svg)]()[![1](images/star6.svg)]()|
|[2](#paper2)|[![1](images/square1.svg)]()|[![1](images/stop-circle5.svg)]()|[![1](images/square.svg)]()|[![1](images/star6.svg)]()|
|[3](#paper3)|[![1](images/square1.svg)]()|[![1](images/stop-circle5.svg)]()|[![1](images/square.svg)]()[![1](images/star.svg)]()[![1](images/stop-circle.svg)]()|[![1](images/star6.svg)]()|
|[4](#paper4)|[![1](images/star1.svg)]()|[![1](images/square5.svg)]()[![1](images/target5.svg)]()|[![1](images/square.svg)]()|[![1](images/square6.svg)]()[![1](images/star6.svg)]()[![1](images/stop-circle6.svg)]()|
|[5](#paper5)|[![1](images/star1.svg)]()|[![1](images/stop-circle5.svg)]()|[![1](images/square.svg)]()|[![1](images/square6.svg)]()|
|[6](#paper6)|[![1](images/square1.svg)]()[![1](images/star1.svg)]()|[![1](images/stop-circle5.svg)]()|[![1](images/square.svg)]()|[![1](images/square6.svg)]()[![1](images/star6.svg)]()|
|[7](#paper7)|[![1](images/square1.svg)]()[![1](images/star1.svg)]()|[![1](images/stop-circle5.svg)]()|[![1](images/square.svg)]()[![1](images/star.svg)]()[![1](images/stop-circle.svg)]()[![1](images/target.svg)]()|[![1](images/square6.svg)]()|
|[8](#paper8)|[![1](images/square1.svg)]()[![1](images/star1.svg)]()|[![1](images/stop-circle5.svg)]()|[![1](images/star.svg)]()|[![1](images/square6.svg)]()[![1](images/star6.svg)]()|
|[9](#paper9)|[![1](images/square1.svg)]()[![1](images/star1.svg)]()|[![1](images/square5.svg)]()[![1](images/stop-circle5.svg)]()[![1](images/target5.svg)]()|[![1](images/square.svg)]()[![1](images/star.svg)]()|[![1](images/square6.svg)]()[![1](images/star6.svg)]()|
|[10](#paper10)|[![1](images/star1.svg)]()[![1](images/stop-circle1.svg)]()|[![1](images/stop-circle5.svg)]()|[![1](images/square.svg)]()[![1](images/star.svg)]()[![1](images/stop-circle.svg)]()[![1](images/target.svg)]()|[![1](images/square6.svg)]()|
|[11](#paper11)|[![1](images/star1.svg)]()[![1](images/stop-circle1.svg)]()|[![1](images/stop-circle5.svg)]()|[![1](images/square.svg)]()[![1](images/star.svg)]()[![1](images/stop-circle.svg)]()[![1](images/target.svg)]()|[![1](images/square6.svg)]()[![1](images/star6.svg)]()|
|[12](#paper12)|[![1](images/square1.svg)]()[![1](images/star1.svg)]()|[![1](images/target5.svg)]()|[![1](images/square.svg)]()|[![1](images/square6.svg)]()[![1](images/star6.svg)]()|
|[13](#paper13)|[![1](images/square1.svg)]()[![1](images/star1.svg)]()|[![1](images/square5.svg)]()[![1](images/target5.svg)]()|[![1](images/star.svg)]()|[![1](images/square6.svg)]()[![1](images/star6.svg)]()|
|[14](#paper14)|[![1](images/square1.svg)]()[![1](images/star1.svg)]()|[![1](images/square5.svg)]()[![1](images/stop-circle5.svg)]()[![1](images/target5.svg)]()|[![1](images/square.svg)]()|[![1](images/square6.svg)]()[![1](images/star6.svg)]()|
|[15](#paper15)|[![1](images/square1.svg)]()[![1](images/star1.svg)]()|[![1](images/target5.svg)]()|[![1](images/square.svg)]()|[![1](images/square6.svg)]()[![1](images/star6.svg)]()|
|[16](#paper16)|[![1](images/star1.svg)]()|[![1](images/target5.svg)]()|[![1](images/target.svg)]()|[![1](images/square6.svg)]()[![1](images/star6.svg)]()|
|[17](#paper17)|[![1](images/star1.svg)]()|[![1](images/stop-circle5.svg)]()|[![1](images/target.svg)]()|[![1](images/square6.svg)]()|
|[18](#paper18)|[![1](images/square1.svg)]()[![1](images/target1.svg)]()|[![1](images/square5.svg)]()[![1](images/stop-circle5.svg)]()[![1](images/target5.svg)]()|[![1](images/target.svg)]()|[![1](images/square6.svg)]()[![1](images/star6.svg)]()[![1](images/stop-circle6.svg)]()|
|[19](#paper19)|[![1](images/star1.svg)]()|[![1](images/square5.svg)]()|[![1](images/square.svg)]()|[![1](images/star6.svg)]()|
|[20](#paper20)|[![1](images/star1.svg)]()|[![1](images/stop-circle5.svg)]()|[![1](images/square.svg)]()|[![1](images/star6.svg)]()|
|[21](#paper21)|[![1](images/target1.svg)]()|[![1](images/square5.svg)]()[![1](images/stop-circle5.svg)]()[![1](images/target5.svg)]()|[![1](images/square.svg)]()|[![1](images/square6.svg)]()[![1](images/star6.svg)]()|
|[22](#paper22)|[![1](images/star1.svg)]()|[![1](images/square5.svg)]()[![1](images/target5.svg)]()|[![1](images/square.svg)]()|[![1](images/star6.svg)]()|
|[23](#paper23)|[![1](images/star1.svg)]()[![1](images/stop-circle1.svg)]()|[![1](images/square5.svg)]()[![1](images/stop-circle5.svg)]()[![1](images/target5.svg)]()|[![1](images/square.svg)]()|[![1](images/square6.svg)]()[![1](images/star6.svg)]()|
|[24](#paper24)|[![1](images/star1.svg)]()|[![1](images/square5.svg)]()[![1](images/target5.svg)]()|[![1](images/target.svg)]()|[![1](images/square6.svg)]()[![1](images/star6.svg)]()|
|[25](#paper25)|[![1](images/square1.svg)]()[![1](images/star1.svg)]()|[![1](images/star5.svg)]()[![1](images/stop-circle5.svg)]()|[![1](images/square.svg)]()[![1](images/star.svg)]()|[![1](images/square6.svg)]()[![1](images/star6.svg)]()|
|[26](#paper26)|[![1](images/star1.svg)]()|[![1](images/square5.svg)]()[![1](images/target5.svg)]()|[![1](images/square.svg)]()|[![1](images/square6.svg)]()[![1](images/star6.svg)]()|
|[27](#paper27)|[![1](images/star1.svg)]()|[![1](images/square5.svg)]()[![1](images/stop-circle5.svg)]()[![1](images/target5.svg)]()|[![1](images/square.svg)]()|[![1](images/square6.svg)]()[![1](images/star6.svg)]()|
|[28](#paper28)|[![1](images/square1.svg)]()[![1](images/star1.svg)]()|[![1](images/target5.svg)]()|[![1](images/square.svg)]()[![1](images/star.svg)]()|[![1](images/square6.svg)]()[![1](images/star6.svg)]()|
|[29](#paper29)|[![1](images/star1.svg)]()|[![1](images/stop-circle5.svg)]()|[![1](images/star.svg)]()|[![1](images/square6.svg)]()|
|[30](#paper30)|[![1](images/square1.svg)]()[![1](images/stop-circle1.svg)]()|[![1](images/square5.svg)]()|[![1](images/star.svg)]()[![1](images/stop-circle.svg)]()|[![1](images/square6.svg)]()[![1](images/star6.svg)]()|
|[31](#paper31)|[![1](images/square1.svg)]()|[![1](images/star5.svg)]()|[![1](images/star.svg)]()[![1](images/stop-circle.svg)]()|[![1](images/square6.svg)]()|
|[32](#paper32)|[![1](images/stop-circle1.svg)]()|[![1](images/square5.svg)]()[![1](images/target5.svg)]()|[![1](images/square.svg)]()[![1](images/star.svg)]()|[![1](images/square6.svg)]()[![1](images/star6.svg)]()|
|[33](#paper33)|[![1](images/target1.svg)]()|[![1](images/target5.svg)]()|[![1](images/square.svg)]()|[![1](images/square6.svg)]()[![1](images/star6.svg)]()[![1](images/stop-circle6.svg)]()|
|[34](#paper34)|[![1](images/target1.svg)]()|[![1](images/target5.svg)]()|[![1](images/square.svg)]()|[![1](images/square6.svg)]()[![1](images/star6.svg)]()|
|[35](#paper35)|[![1](images/target1.svg)]()|[![1](images/target5.svg)]()|[![1](images/square.svg)]()[![1](images/star.svg)]()|[![1](images/square6.svg)]()[![1](images/star6.svg)]()|
|[36](#paper36)|[![1](images/stop-circle1.svg)]()|[![1](images/square5.svg)]()[![1](images/target5.svg)]()|[![1](images/square.svg)]()|[![1](images/square6.svg)]()[![1](images/star6.svg)]()|
|[37](#paper37)|[![1](images/stop-circle1.svg)]()|[![1](images/square5.svg)]()[![1](images/target5.svg)]()|[![1](images/square.svg)]()|[![1](images/square6.svg)]()[![1](images/star6.svg)]()|
|[38](#paper38)|[![1](images/star1.svg)]()[![1](images/stop-circle1.svg)]()|[![1](images/square5.svg)]()[![1](images/target5.svg)]()|[![1](images/square.svg)]()|[![1](images/square6.svg)]()[![1](images/star6.svg)]()[![1](images/stop-circle6.svg)]()|
|[39](#paper39)|[![1](images/square1.svg)]()|[![1](images/square5.svg)]()|[![1](images/square.svg)]()[![1](images/star.svg)]()|[![1](images/star6.svg)]()|
|[40](#paper40)|[![1](images/target1.svg)]()|[![1](images/square5.svg)]()|[![1](images/square.svg)]()[![1](images/star.svg)]()|[![1](images/square6.svg)]()[![1](images/star6.svg)]()|
|[41](#paper41)|[![1](images/square1.svg)]()|[![1](images/star5.svg)]()|[![1](images/square.svg)]()[![1](images/star.svg)]()|[![1](images/square6.svg)]()[![1](images/star6.svg)]()|
|[42](#paper42)|[![1](images/target1.svg)]()|[![1](images/square5.svg)]()[![1](images/stop-circle5.svg)]()[![1](images/target5.svg)]()|[![1](images/target.svg)]()|[![1](images/square6.svg)]()[![1](images/star6.svg)]()[![1](images/stop-circle6.svg)]()|
|[43](#paper43)|[![1](images/square1.svg)]()|[![1](images/square5.svg)]()[![1](images/target5.svg)]()|[![1](images/star.svg)]()|[![1](images/square6.svg)]()[![1](images/star6.svg)]()|
|[44](#paper44)|[![1](images/square1.svg)]()|[![1](images/square5.svg)]()[![1](images/target5.svg)]()|[![1](images/square.svg)]()[![1](images/star.svg)]()|[![1](images/star6.svg)]()|
|[45](#paper45)|[![1](images/square1.svg)]()|[![1](images/target5.svg)]()|[![1](images/square.svg)]()[![1](images/star.svg)]()|[![1](images/star6.svg)]()|
|[46](#paper46)|[![1](images/square1.svg)]()|[![1](images/square5.svg)]()[![1](images/stop-circle5.svg)]()[![1](images/target5.svg)]()|[![1](images/square.svg)]()[![1](images/star.svg)]()[![1](images/stop-circle.svg)]()[![1](images/target.svg)]()|[![1](images/square6.svg)]()|
|[47](#paper47)|[![1](images/star1.svg)]()|[![1](images/square5.svg)]()[![1](images/stop-circle5.svg)]()|[![1](images/square.svg)]()|[![1](images/square6.svg)]()[![1](images/star6.svg)]()[![1](images/stop-circle6.svg)]()|
|[48](#paper48)|[![1](images/square1.svg)]()[![1](images/star1.svg)]()|[![1](images/square5.svg)]()[![1](images/star5.svg)]()[![1](images/stop-circle5.svg)]()|[![1](images/square.svg)]()|[![1](images/square6.svg)]()[![1](images/star6.svg)]()|
|[49](#paper49)|[![1](images/square1.svg)]()|[![1](images/target5.svg)]()|[![1](images/square.svg)]()|[![1](images/square6.svg)]()[![1](images/star6.svg)]()|
|[50](#paper50)|[![1](images/target1.svg)]()|[![1](images/target5.svg)]()|[![1](images/square.svg)]()|[![1](images/square6.svg)]()[![1](images/star6.svg)]()|
|[51](#paper51)|[![1](images/stop-circle1.svg)]()|[![1](images/target5.svg)]()|[![1](images/square.svg)]()|[![1](images/star6.svg)]()|
|[52](#paper52)|[![1](images/square1.svg)]()|[![1](images/target5.svg)]()|[![1](images/square.svg)]()[![1](images/star.svg)]()[![1](images/stop-circle.svg)]()[![1](images/target.svg)]()|[![1](images/star6.svg)]()|
|[53](#paper53)|[![1](images/target1.svg)]()|[![1](images/target5.svg)]()|[![1](images/square.svg)]()[![1](images/star.svg)]()|[![1](images/square6.svg)]()[![1](images/star6.svg)]()|
|[54](#paper54)|[![1](images/star1.svg)]()|[![1](images/stop-circle5.svg)]()|[![1](images/square.svg)]()[![1](images/star.svg)]()[![1](images/stop-circle.svg)]()[![1](images/target.svg)]()|[![1](images/square6.svg)]()|
|[55](#paper55)|[![1](images/stop-circle1.svg)]()|[![1](images/target5.svg)]()|[![1](images/square.svg)]()|[![1](images/star6.svg)]()|
|[56](#paper56)|[![1](images/star1.svg)]()|[![1](images/stop-circle5.svg)]()|[![1](images/square.svg)]()[![1](images/star.svg)]()[![1](images/stop-circle.svg)]()[![1](images/target.svg)]()|[![1](images/square6.svg)]()|

| ID | Venue  | Title | Affiliation | &nbsp;&nbsp;&nbsp;&nbsp;Link&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 
| :-: | :-: | :----: | :---------: | :---: |
1<a name='paper1'></a>|Arxiv <br>2020|Carbontracker: Tracking and Predicting the Carbon Footprint of Training Deep Learning Models|UCPH| [[paper]](https://Arxiv.org/abs/2007.03051)![Scholar citations](https://img.shields.io/badge/Citations-230-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
2<a name='paper2'></a>|TCADICS  <br>2022|ESSENCE: Exploiting Structured Stochastic Gradient Pruning for Endurance-Aware ReRAM-Based In-Memory Training Systems|Duke| [[paper]](https://ieeexplore.ieee.org/document/9926186)![Scholar citations](https://img.shields.io/badge/Citations-2-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
3<a name='paper3'></a>|ICCAD <br>2020|ReTransformer: ReRAM-based Processing-in-Memory Architecture for Transformer Acceleration|Duke | [[paper]](https://ieeexplore.ieee.org/document/9256523)![Scholar citations](https://img.shields.io/badge/Citations-38-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
4<a name='paper4'></a>|HPCA <br>2022|Chasing Carbon: The Elusive Environmental Footprint of Computing|Harvard | [[paper]](https://Arxiv.org/pdf/2011.02839.pdf)![Scholar citations](https://img.shields.io/badge/Citations-154-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
5<a name='paper5'></a>|RSER <br>2023|Assessing embodied carbon emissions of communication user devices by combining approaches|Ericsson Research| [[paper]](https://www.sciencedirect.com/science/article/pii/S1364032123002794)![Scholar citations](https://img.shields.io/badge/Citations-1-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
6<a name='paper6'></a>|ASPLOS <br>2023|Carbon Explorer: A Holistic Framework for Designing Carbon Aware Datacenters|Meta| [[paper]](https://Arxiv.org/pdf/2201.10036.pdf)![Scholar citations](https://img.shields.io/badge/Citations-24-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
7<a name='paper7'></a>|Arxiv <br>2023|Towards Sustainable Computing: Accessing the Cabon Footprint of Heterogeneous Systems|ASU| [[paper]](https://Arxiv.org/abs/2306.09434)![Scholar citations](https://img.shields.io/badge/Citations-0-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
8<a name='paper8'></a>|Micro <br>2022|Sustainable AI Processing at the Edge|PITT| [[paper]](https://Arxiv.org/pdf/2207.01209.pdf)![Scholar citations](https://img.shields.io/badge/Citations-2-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
9<a name='paper9'></a>|Arxiv <br>2023|When the Metaverse Meets Carbon Neutrality: Ongoing Efforts and Directions|HUST| [[paper]](https://Arxiv.org/pdf/2301.10235.pdf)![Scholar citations](https://img.shields.io/badge/Citations-4-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
10<a name='paper10'></a>|ISCA <br>2022|ACT: Designing sustainable computer systems with an architectural carbon modeling tool|Harvard| [[paper]](https://ieeexplore.ieee.org/document/10122998)![Scholar citations](https://img.shields.io/badge/Citations-37-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
11<a name='paper11'></a>|Arxiv <br>2023|Design space exploration and optimization for carbon-efficient extended reality systems|Harvard | [[paper]](https://Arxiv.org/abs/2305.01831)![Scholar citations](https://img.shields.io/badge/Citations-2-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
12<a name='paper12'></a>|FACCT <br>2022|Measuring the Carbon Intensity of AI in Cloud Instances|AI2| [[paper]](https://dl.acm.org/doi/pdf/10.1145/3531146.3533234)![Scholar citations](https://img.shields.io/badge/Citations-51-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
13<a name='paper13'></a>|Arxiv <br>2023|GreenScale: Carbon-Aware Systems for Edge Computing|KU| [[paper]](https://Arxiv.org/pdf/2304.00404.pdf)![Scholar citations](https://img.shields.io/badge/Citations-0-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
14<a name='paper14'></a>|MLSys <br>2022|Sustainable AI: Environmental Implications, Challenges and Opportunities|Meta | [[paper]](https://proceedings.mlsys.org/paper_files/paper/2022/file/462211f67c7d858f663355eff93b745e-Paper.pdf)![Scholar citations](https://img.shields.io/badge/Citations-127-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
15<a name='paper15'></a>|HotCarbon <br>2023|Peeling Back the Carbon Curtain: Carbon Optimization Challenges in Cloud Computing|CMU| [[paper]](https://hotcarbon.org/2023/pdf/a8-wang.pdf)![Scholar citations](https://img.shields.io/badge/Citations-0-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
16<a name='paper16'></a>|Arxiv <br>2023|Is TinyML Sustainable?Assessing the Environmental Impacts of Machine Learning on Microcontrollers|Harvard| [[paper]](https://Arxiv.org/pdf/2301.11899.pdf)![Scholar citations](https://img.shields.io/badge/Citations-0-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
17<a name='paper17'></a>|JCP <br>2021|Assessing the embodied carbon footprint of IoT edge devices with a bottom-up life-cycle approach|UCLouvain| [[paper]](https://Arxiv.org/abs/2105.02082)![Scholar citations](https://img.shields.io/badge/Citations-39-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
18<a name='paper18'></a>|ICAIS <br>2023|Carbon Neutrality Approaches for IoT-Enabled Applications|IIIKT| [[paper]](https://ieeexplore.ieee.org/document/10073921)![Scholar citations](https://img.shields.io/badge/Citations-0-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
19<a name='paper19'></a>|ECEE <br>2023|Sustainability of Machine Learning Models: An Energy Consumption Centric Evaluation|LBU| [[paper]](https://ieeexplore.ieee.org/document/10101532)![Scholar citations](https://img.shields.io/badge/Citations-0-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
20<a name='paper20'></a>|Arxiv <br>2023|XGen-7B Technical Report|SFR| [[paper]](https://Arxiv.org/pdf/2309.03450.pdf)![Scholar citations](https://img.shields.io/badge/Citations-0-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
21<a name='paper21'></a>|ERC <br>2023|How to estimate carbon footprint when training deep learning models? A guide and review|Cité U| [[paper]](https://iopscience.iop.org/article/10.1088/2515-7620/acf81b/pdf)![Scholar citations](https://img.shields.io/badge/Citations-0-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
22<a name='paper22'></a>|Arxiv <br>2021|Carbon Emissions and Large Neural Network Training|UCB| [[paper]](https://Arxiv.org/pdf/2104.10350)![Scholar citations](https://img.shields.io/badge/Citations-360-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
23<a name='paper23'></a>|IJEEE <br>2022|Capping carbon emission from green data centers|UAuburn| [[paper]](https://link.springer.com/article/10.1007/s40095-022-00539-9)![Scholar citations](https://img.shields.io/badge/Citations-3-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
24<a name='paper24'></a>|SEGN <br>2020|The global energy footprint of information and communication technology electronics in connected Internet-of-Things devices|ORNL| [[paper]](sciencedirect.com/science/article/pii/S2352467720303398#sec4)![Scholar citations](https://img.shields.io/badge/Citations-32-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
25<a name='paper25'></a>|Hotcarbon <br>2023|Carbon-Aware Memory Placement|UPotsdam| [[paper]](https://dl.acm.org/doi/abs/10.1145/3604930.3605714)![Scholar citations](https://img.shields.io/badge/Citations-0-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
26<a name='paper26'></a>|TPS <br>2021|Carbon-Aware Computing for Datacenters|Google| [[paper]](https://ieeexplore.ieee.org/document/9770383?denied=)![Scholar citations](https://img.shields.io/badge/Citations-69-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
27<a name='paper27'></a>|Arxiv <br>2023|Sustainable HPC: Modeling, Characterization, and Implications of Carbon Footprint in Modern HPC Systems|Northeastern University| [[paper]](https://Arxiv.org/abs/2306.13177)![Scholar citations](https://img.shields.io/badge/Citations-0-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
28<a name='paper28'></a>|GLOBECOM <br>2022|Carbon-Neutralized Task Scheduling for Green Computing Networks|MediaTek | [[paper]](https://Arxiv.org/abs/2209.02198)![Scholar citations](https://img.shields.io/badge/Citations-3-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
29<a name='paper29'></a>|RSER <br>2023|Assessing embodied carbon emissions of communication user devices by combining approaches|Ericsson Research| [[paper]](https://www.sciencedirect.com/science/article/pii/S1364032123002794)![Scholar citations](https://img.shields.io/badge/Citations-1-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
30<a name='paper30'></a>|HotCarbon <br>2023|Towards Application Centric Carbon Emission Management|RU| [[paper]](https://dl.acm.org/doi/abs/10.1145/3604930.3605725)![Scholar citations](https://img.shields.io/badge/Citations-0-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
31<a name='paper31'></a>|HotCarbon <br>2023|carbond: An Operating-System Daemon for Carbon Awareness|SIC| [[paper]](https://dl.acm.org/doi/abs/10.1145/3604930.3605707)![Scholar citations](https://img.shields.io/badge/Citations-0-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
32<a name='paper32'></a>|HotCarbon <br>2023|Bringing Carbon Awareness to Multi-cloud Application Delivery|UMA| [[paper]](https://hotcarbon.org/2023/pdf/a6-maji.pdf)![Scholar citations](https://img.shields.io/badge/Citations-0-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
33<a name='paper33'></a>|HotCarbon <br>2024|Myths and Misconceptions Around Reducing Carbon Embedded in Cloud Platforms|UToronto| [[paper]](https://hotcarbon.org/2023/pdf/a7-lyu.pdf)![Scholar citations](https://img.shields.io/badge/Citations-0-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
34<a name='paper34'></a>|HotCarbon <br>2023|Towards Carbon Footprint Management in Hybrid Multicloud|IBM| [[paper]](https://hotcarbon.org/2023/pdf/a9-arora.pdf)![Scholar citations](https://img.shields.io/badge/Citations-0-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
35<a name='paper35'></a>|HotCarbon <br>2023|An Agile Pathway Towards Carbon-aware Clouds|UW| [[paper]](https://hotcarbon.org/2023/pdf/a10-patel.pdf)![Scholar citations](https://img.shields.io/badge/Citations-0-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
36<a name='paper36'></a>|HotCarbon <br>2022|Metrics for Sustainability in Data Centers|SBU| [[paper]](https://hotcarbon.org/2022/pdf/hotcarbon22-gandhi.pdf)![Scholar citations](https://img.shields.io/badge/Citations-6-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
37<a name='paper37'></a>|HotCarbon <br>2023|Towards a Methodology and Framework for AI Sustainability Metrics|IBM| [[paper]](https://hotcarbon.org/2023/pdf/a13-eilam.pdf)![Scholar citations](https://img.shields.io/badge/Citations-0-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
38<a name='paper38'></a>|HotCarbon <br>2023|Toward a Life Cycle Assessment for the Carbon Footprint of Data|UChicago| [[paper]](https://hotcarbon.org/2023/pdf/a14-mersy.pdf)![Scholar citations](https://img.shields.io/badge/Citations-0-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
39<a name='paper39'></a>|HotCarbon <br>2023|Carbon-Efficient Neural Architecture Search|WPI| [[paper]](https://hotcarbon.org/2023/pdf/a12-zhao.pdf)![Scholar citations](https://img.shields.io/badge/Citations-0-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
40<a name='paper40'></a>|HotCarbon <br>2023|Reducing the Carbon Impact of Generative AI Inference (today and in 2035)|UChicago| [[paper]](https://hotcarbon.org/2023/pdf/a11-chien.pdf)![Scholar citations](https://img.shields.io/badge/Citations-0-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
41<a name='paper41'></a>|HotCarbon <br>2023|Carbon-Efficient Design Optimization for Computing Systems|Harvard| [[paper]](https://hotcarbon.org/2023/pdf/a16-elgamal.pdf)![Scholar citations](https://img.shields.io/badge/Citations-0-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
42<a name='paper42'></a>|JNCA <br>2022|Recent advances in energy management for Green-IoT: An up-to-date and comprehensive survey|USorbonne| [[paper]](https://www.sciencedirect.com/science/article/pii/S1084804521002551)![Scholar citations](https://img.shields.io/badge/Citations-42-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
43<a name='paper43'></a>|IEEE Networking Letters <br>2023|Less Carbon Footprint in Edge Computing by Joint Task Offloading and Energy Sharing|UUMS| [[paper]](https://ieeexplore.ieee.org/abstract/document/10154013)![Scholar citations](https://img.shields.io/badge/Citations-1-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
44<a name='paper44'></a>|IMCOM <br>2023|Lightweight energy-efficient offloading framework for mobile edge/cloud computing|NU| [[paper]](https://ieeexplore.ieee.org/abstract/document/10035628)![Scholar citations](https://img.shields.io/badge/Citations-0-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
45<a name='paper45'></a>|ICICC <br>2022|Shifting from Cloud Computing to Green Cloud and Edge Computing|NHU| [[paper]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4387781)![Scholar citations](https://img.shields.io/badge/Citations-1-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
46<a name='paper46'></a>|HotCarbon <br>2023|On the Promise and Pitfalls of Optimizing Embodied Carbon|UMASS| [[paper]](https://dl.acm.org/doi/abs/10.1145/3604930.3605710)![Scholar citations](https://img.shields.io/badge/Citations-1-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
47<a name='paper47'></a>|MICCAI <br>2022|Carbon Footprint of Selecting and Training Deep Learning Models for Medical Image Analysis|UCPH| [[paper]](https://Arxiv.org/pdf/2203.02202.pdf)![Scholar citations](https://img.shields.io/badge/Citations-14-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
48<a name='paper48'></a>|HotCarbon <br>2023|EnergAt: Fine-Grained Energy Attribution for Multi-Tenancy|ETH| [[paper]](https://Arxiv.org/abs/2307.05647)![Scholar citations](https://img.shields.io/badge/Citations-0-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
49<a name='paper49'></a>|HotCarbon <br>2022|Carbon Dependencies in Datacenter Design and Management|Meta| [[paper]](https://hotcarbon.org/2022/pdf/hotcarbon22-acun.pdf)![Scholar citations](https://img.shields.io/badge/Citations-2-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
50<a name='paper50'></a>|Arxiv <br>2021|Towards a systematic survey for carbon neutral data centers.|NTU| [[paper]](https://Arxiv.org/abs/2110.09284)![Scholar citations](https://img.shields.io/badge/Citations-21-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
51<a name='paper51'></a>|HotCarbon <br>2022|Beyond PUE: Flexible Datacenters Empowering the Cloud to Decarbonize|UChicago| [[paper]](https://hotcarbon.org/2022/pdf/hotcarbon22-chien.pdf)![Scholar citations](https://img.shields.io/badge/Citations-6-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
52<a name='paper52'></a>|HotCarbon <br>2022|Multiple smaller base stations are greener than a single powerful one: Densification of Wireless Cellular Networks|UCSD| [[paper]](https://hotcarbon.org/2022/pdf/hotcarbon22-gupta.pdf)![Scholar citations](https://img.shields.io/badge/Citations-1-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
53<a name='paper53'></a>|HotCarbon <br>2022|Toward Carbon-Aware Networking|Ox| [[paper]](https://hotcarbon.org/2022/pdf/hotcarbon22-zilberman.pdf)![Scholar citations](https://img.shields.io/badge/Citations-2-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
54<a name='paper54'></a>|HotCarbon <br>2022|The Dirty Secret of SSDs: Embodied Carbon|UWM| [[paper]](https://Arxiv.org/abs/2207.10793)![Scholar citations](https://img.shields.io/badge/Citations-9-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
55<a name='paper55'></a>|ICACT <br>2019|PUE or GPUE: A Carbon-Aware Metric for Data Centers|KAIST| [[paper]](https://ieeexplore.ieee.org/document/8701895)![Scholar citations](https://img.shields.io/badge/Citations-4-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
56<a name='paper56'></a>|RCR <br>2022|Life cycle assessment of emerging technologies on value recovery from hard disk drives.|UA| [[paper]](https://www.sciencedirect.com/science/article/pii/S0921344920301026)![Scholar citations](https://img.shields.io/badge/Citations-38-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|
## Contribute

We welcome contributions to [this repository](https://github.com/zhaoyujieseberena/Carbon). To add new papers to this list, please update csv files under `./res/papers.csv`. Our bots will update the paper list in `README.md` automatically. The citations of newly added papers will be updated within one day.
