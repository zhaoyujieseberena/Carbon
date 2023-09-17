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

| Target Problem                                  | Computer system stack                             | Hardware system                    | Carbon life cycle stage(s)                  |
| ----------------------------------------------- | ------------------------------------------------- | ---------------------------------- | ------------------------------------------- |
| ![1](images/square (1).svg)Optimation           | ![1](images/square (5).svg) Application           | ![1](images/square.svg)Datacenter  | ![1](images/square (6).svg)Manufacturing    |
| ![1](images/star (1).svg)Modeling               | ![1](images/star (5).svg)OS                       | ![1](images/star.svg)Edge          | ![1](images/star (6).svg)Operation          |
| ![1](images/stop-circle (1).svg)Standardization | ![1](images/stop-circle (5).svg)Microarchitecture | ![1](images/stop-circle.svg)Mobile | ![1](images/stop-circle (6).svg)End-of-life |
| ![1](images/target (1).svg)Review               | ![1](images/target (5).svg)Infrastructure         | ![1](images/target.svg)TinyML      |                                             |
## Metrics
| Metric | Computer system stack | Hardware system | Carbon life cycle stage(s) | 
| :---: | :------: | :------: | :--------: | 
|PUE|[![1](images/target (5).svg)]()|[![1](images/square.svg)]()|[![1](images/star (6).svg)]()|
|GPUE|[![1](images/target (5).svg)]()|[![1](images/square.svg)]()|[![1](images/star (6).svg)]()|
|CUE|[![1](images/target (5).svg)]()|[![1](images/square.svg)]()|[![1](images/star (6).svg)]()|
|CCI|[![1](images/target (5).svg)]()|[![1](images/square.svg)]()|[![1](images/star (6).svg)]()|
|SCI|[![1](images/square (5).svg)]()|[![1](images/square.svg)]()[![1](images/star.svg)]()[![1](images/stop-circle.svg)]()|[![1](images/square (6).svg)]()[![1](images/star (6).svg)]()|
|CDP/CEP|[![1](images/stop-circle (5).svg)]()|[![1](images/square.svg)]()[![1](images/star.svg)]()[![1](images/stop-circle.svg)]()|[![1](images/square (6).svg)]()[![1](images/star (6).svg)]()|
|tCDP/tCEP|[![1](images/stop-circle (5).svg)]()|[![1](images/square.svg)]()[![1](images/star.svg)]()[![1](images/stop-circle.svg)]()|[![1](images/square (6).svg)]()[![1](images/star (6).svg)]()|
|JSC|[![1](images/square (5).svg)]()|[![1](images/square.svg)]()[![1](images/star.svg)]()[![1](images/stop-circle.svg)]()|[![1](images/square (6).svg)]()[![1](images/star (6).svg)]()|
|ASC|[![1](images/square (5).svg)]()|[![1](images/square.svg)]()[![1](images/star.svg)]()[![1](images/stop-circle.svg)]()|[![1](images/square (6).svg)]()[![1](images/star (6).svg)]()|

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
| Paper | Computer system stack | Hardware system ｜ Target Problem | Carbon life cycle stage(s) | 
| :---: | :------: | :------: | :--------: | :--------: | 
|1|1|[![1](images/square.svg)]()[![1](images/star.svg)]()|[![1](images/star (1).svg)]()|[![1](images/square (6).svg)]()[![1](images/star (6).svg)]()|
|2|1|[![1](images/square.svg)]()|[![1](images/square (1).svg)]()|[![1](images/star (6).svg)]()|
|3|1|[![1](images/square.svg)]()[![1](images/star.svg)]()[![1](images/stop-circle.svg)]()|[![1](images/square (1).svg)]()|[![1](images/star (6).svg)]()|
|4|1|[![1](images/square.svg)]()|[![1](images/star (1).svg)]()|[![1](images/square (6).svg)]()[![1](images/star (6).svg)]()[![1](images/stop-circle (6).svg)]()|
|5|1|[![1](images/square.svg)]()|[![1](images/star (1).svg)]()|[![1](images/square (6).svg)]()|
|6|1|[![1](images/square.svg)]()|[![1](images/square (1).svg)]()[![1](images/star (1).svg)]()|[![1](images/square (6).svg)]()[![1](images/star (6).svg)]()|
|7|1|[![1](images/square.svg)]()[![1](images/star.svg)]()[![1](images/stop-circle.svg)]()[![1](images/target.svg)]()|[![1](images/square (1).svg)]()[![1](images/star (1).svg)]()|[![1](images/square (6).svg)]()|
|8|1|[![1](images/star.svg)]()|[![1](images/square (1).svg)]()[![1](images/star (1).svg)]()|[![1](images/square (6).svg)]()[![1](images/star (6).svg)]()|
|9|1|[![1](images/square.svg)]()[![1](images/star.svg)]()|[![1](images/square (1).svg)]()[![1](images/star (1).svg)]()|[![1](images/square (6).svg)]()[![1](images/star (6).svg)]()|
|10|1|[![1](images/square.svg)]()[![1](images/star.svg)]()[![1](images/stop-circle.svg)]()[![1](images/target.svg)]()|[![1](images/star (1).svg)]()[![1](images/stop-circle (1).svg)]()|[![1](images/square (6).svg)]()|
|11|1|[![1](images/square.svg)]()[![1](images/star.svg)]()[![1](images/stop-circle.svg)]()[![1](images/target.svg)]()|[![1](images/star (1).svg)]()[![1](images/stop-circle (1).svg)]()|[![1](images/square (6).svg)]()[![1](images/star (6).svg)]()|
|12|1|[![1](images/square.svg)]()|[![1](images/square (1).svg)]()[![1](images/star (1).svg)]()|[![1](images/square (6).svg)]()[![1](images/star (6).svg)]()|
|13|1|[![1](images/star.svg)]()|[![1](images/square (1).svg)]()[![1](images/star (1).svg)]()|[![1](images/square (6).svg)]()[![1](images/star (6).svg)]()|
|14|1|[![1](images/square.svg)]()|[![1](images/square (1).svg)]()[![1](images/star (1).svg)]()|[![1](images/square (6).svg)]()[![1](images/star (6).svg)]()|
|15|1|[![1](images/square.svg)]()|[![1](images/square (1).svg)]()[![1](images/star (1).svg)]()|[![1](images/square (6).svg)]()[![1](images/star (6).svg)]()|
|16|1|[![1](images/target.svg)]()|[![1](images/star (1).svg)]()|[![1](images/square (6).svg)]()[![1](images/star (6).svg)]()|
|17|1|[![1](images/target.svg)]()|[![1](images/star (1).svg)]()|[![1](images/square (6).svg)]()|
|18|1|[![1](images/target.svg)]()|[![1](images/square (1).svg)]()[![1](images/target (1).svg)]()|[![1](images/square (6).svg)]()[![1](images/star (6).svg)]()[![1](images/stop-circle (6).svg)]()|
|19|1|[![1](images/square.svg)]()|[![1](images/star (1).svg)]()|[![1](images/star (6).svg)]()|
|20|1|[![1](images/square.svg)]()|[![1](images/star (1).svg)]()|[![1](images/star (6).svg)]()|
|21|1|[![1](images/square.svg)]()|[![1](images/target (1).svg)]()|[![1](images/square (6).svg)]()[![1](images/star (6).svg)]()|
|22|1|[![1](images/square.svg)]()|[![1](images/star (1).svg)]()|[![1](images/star (6).svg)]()|
|23|1|[![1](images/square.svg)]()|[![1](images/star (1).svg)]()[![1](images/stop-circle (1).svg)]()|[![1](images/square (6).svg)]()[![1](images/star (6).svg)]()|
|24|1|[![1](images/target.svg)]()|[![1](images/star (1).svg)]()|[![1](images/square (6).svg)]()[![1](images/star (6).svg)]()|
|25|1|[![1](images/square.svg)]()[![1](images/star.svg)]()|[![1](images/square (1).svg)]()[![1](images/star (1).svg)]()|[![1](images/square (6).svg)]()[![1](images/star (6).svg)]()|
|26|1|[![1](images/square.svg)]()|[![1](images/star (1).svg)]()|[![1](images/square (6).svg)]()[![1](images/star (6).svg)]()|
|27|1|[![1](images/square.svg)]()|[![1](images/star (1).svg)]()|[![1](images/square (6).svg)]()[![1](images/star (6).svg)]()|
|28|1|[![1](images/square.svg)]()[![1](images/star.svg)]()|[![1](images/square (1).svg)]()[![1](images/star (1).svg)]()|[![1](images/square (6).svg)]()[![1](images/star (6).svg)]()|
|29|1|[![1](images/star.svg)]()|[![1](images/star (1).svg)]()|[![1](images/square (6).svg)]()|
|30|1|[![1](images/star.svg)]()[![1](images/stop-circle.svg)]()|[![1](images/square (1).svg)]()[![1](images/stop-circle (1).svg)]()|[![1](images/square (6).svg)]()[![1](images/star (6).svg)]()|
|31|1|[![1](images/star.svg)]()[![1](images/stop-circle.svg)]()|[![1](images/square (1).svg)]()|[![1](images/square (6).svg)]()|
|32|1|[![1](images/square.svg)]()[![1](images/star.svg)]()|[![1](images/stop-circle (1).svg)]()|[![1](images/square (6).svg)]()[![1](images/star (6).svg)]()|
|33|1|[![1](images/square.svg)]()|[![1](images/target (1).svg)]()|[![1](images/square (6).svg)]()[![1](images/star (6).svg)]()[![1](images/stop-circle (6).svg)]()|
|34|1|[![1](images/square.svg)]()|[![1](images/target (1).svg)]()|[![1](images/square (6).svg)]()[![1](images/star (6).svg)]()|
|35|1|[![1](images/square.svg)]()[![1](images/star.svg)]()|[![1](images/target (1).svg)]()|[![1](images/square (6).svg)]()[![1](images/star (6).svg)]()|
|36|1|[![1](images/square.svg)]()|[![1](images/stop-circle (1).svg)]()|[![1](images/square (6).svg)]()[![1](images/star (6).svg)]()|
|37|1|[![1](images/square.svg)]()|[![1](images/stop-circle (1).svg)]()|[![1](images/square (6).svg)]()[![1](images/star (6).svg)]()|
|38|1|[![1](images/square.svg)]()|[![1](images/star (1).svg)]()[![1](images/stop-circle (1).svg)]()|[![1](images/square (6).svg)]()[![1](images/star (6).svg)]()[![1](images/stop-circle (6).svg)]()|
|39|1|[![1](images/square.svg)]()[![1](images/star.svg)]()|[![1](images/square (1).svg)]()|[![1](images/star (6).svg)]()|
|40|1|[![1](images/square.svg)]()[![1](images/star.svg)]()|[![1](images/target (1).svg)]()|[![1](images/square (6).svg)]()[![1](images/star (6).svg)]()|
|41|1|[![1](images/square.svg)]()[![1](images/star.svg)]()|[![1](images/square (1).svg)]()|[![1](images/square (6).svg)]()[![1](images/star (6).svg)]()|
|42|1|[![1](images/target.svg)]()|[![1](images/target (1).svg)]()|[![1](images/square (6).svg)]()[![1](images/star (6).svg)]()[![1](images/stop-circle (6).svg)]()|
|43|1|[![1](images/star.svg)]()|[![1](images/square (1).svg)]()|[![1](images/square (6).svg)]()[![1](images/star (6).svg)]()|
|44|1|[![1](images/square.svg)]()[![1](images/star.svg)]()|[![1](images/square (1).svg)]()|[![1](images/star (6).svg)]()|
|45|1|[![1](images/square.svg)]()[![1](images/star.svg)]()|[![1](images/square (1).svg)]()|[![1](images/star (6).svg)]()|
|46|1|[![1](images/square.svg)]()[![1](images/star.svg)]()[![1](images/stop-circle.svg)]()[![1](images/target.svg)]()|[![1](images/square (1).svg)]()|[![1](images/square (6).svg)]()|
|47|1|[![1](images/square.svg)]()|[![1](images/star (1).svg)]()|[![1](images/square (6).svg)]()[![1](images/star (6).svg)]()[![1](images/stop-circle (6).svg)]()|
|48|1|[![1](images/square.svg)]()|[![1](images/square (1).svg)]()[![1](images/star (1).svg)]()|[![1](images/square (6).svg)]()[![1](images/star (6).svg)]()|
|49|1|[![1](images/square.svg)]()|[![1](images/square (1).svg)]()|[![1](images/square (6).svg)]()[![1](images/star (6).svg)]()|
|50|1|[![1](images/square.svg)]()|[![1](images/target (1).svg)]()|[![1](images/square (6).svg)]()[![1](images/star (6).svg)]()|
|51|1|[![1](images/square.svg)]()|[![1](images/stop-circle (1).svg)]()|[![1](images/star (6).svg)]()|
|52|1|[![1](images/square.svg)]()[![1](images/star.svg)]()[![1](images/stop-circle.svg)]()[![1](images/target.svg)]()|[![1](images/square (1).svg)]()|[![1](images/star (6).svg)]()|
|53|1|[![1](images/square.svg)]()[![1](images/star.svg)]()|[![1](images/target (1).svg)]()|[![1](images/square (6).svg)]()[![1](images/star (6).svg)]()|
|54|1|[![1](images/square.svg)]()[![1](images/star.svg)]()[![1](images/stop-circle.svg)]()[![1](images/target.svg)]()|[![1](images/star (1).svg)]()|[![1](images/square (6).svg)]()|
|55|1|[![1](images/square.svg)]()|[![1](images/stop-circle (1).svg)]()|[![1](images/star (6).svg)]()|
|56|1|[![1](images/square.svg)]()[![1](images/star.svg)]()[![1](images/stop-circle.svg)]()[![1](images/target.svg)]()|[![1](images/star (1).svg)]()|[![1](images/square (6).svg)]()|
| Venue  | Title | Affiliation | &nbsp;&nbsp;&nbsp;&nbsp;Link&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 
| :-: | :----: | :---------: | :---: |
|Arxiv <br>2020|Carbontracker: Tracking and Predicting the Carbon Footprint of Training Deep Learning Models|UCPH| [[paper]](https://Arxiv.org/abs/2007.03051)![Scholar citations](https://img.shields.io/badge/Citations-1-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|TCADICS  <br>2022|ESSENCE: Exploiting Structured Stochastic Gradient Pruning for Endurance-Aware ReRAM-Based In-Memory Training Systems|Duke| [[paper]](https://ieeexplore.ieee.org/document/9926186)![Scholar citations](https://img.shields.io/badge/Citations-1-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|ICCAD <br>2020|ReTransformer: ReRAM-based Processing-in-Memory Architecture for Transformer Acceleration|Duke | [[paper]](https://ieeexplore.ieee.org/document/9256523)![Scholar citations](https://img.shields.io/badge/Citations-1-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|HPCA <br>2022|Chasing Carbon: The Elusive Environmental Footprint of Computing|Harvard | [[paper]](https://Arxiv.org/pdf/2011.02839.pdf)![Scholar citations](https://img.shields.io/badge/Citations-1-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|RSER <br>2023|Assessing embodied carbon emissions of communication user devices by combining approaches|Ericsson Research| [[paper]](https://www.sciencedirect.com/science/article/pii/S1364032123002794)![Scholar citations](https://img.shields.io/badge/Citations-1-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|ASPLOS <br>2023|Carbon Explorer: A Holistic Framework for Designing Carbon Aware Datacenters|Meta| [[paper]](https://Arxiv.org/pdf/2201.10036.pdf)![Scholar citations](https://img.shields.io/badge/Citations-1-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|Arxiv <br>2023|Towards Sustainable Computing: Accessing the Cabon Footprint of Heterogeneous Systems|ASU| [[paper]](https://Arxiv.org/abs/2306.09434)![Scholar citations](https://img.shields.io/badge/Citations-1-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|Micro <br>2022|Sustainable AI Processing at the Edge|PITT| [[paper]](https://Arxiv.org/pdf/2207.01209.pdf)![Scholar citations](https://img.shields.io/badge/Citations-1-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|Arxiv <br>2023|When the Metaverse Meets Carbon Neutrality: Ongoing Efforts and Directions|HUST| [[paper]](https://Arxiv.org/pdf/2301.10235.pdf)![Scholar citations](https://img.shields.io/badge/Citations-1-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|ISCA <br>2022|ACT: Designing sustainable computer systems with an architectural carbon modeling tool|Harvard| [[paper]](https://ieeexplore.ieee.org/document/10122998)![Scholar citations](https://img.shields.io/badge/Citations-1-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|Arxiv <br>2023|Design space exploration and optimization for carbon-efficient extended reality systems|Harvard | [[paper]](https://Arxiv.org/abs/2305.01831)![Scholar citations](https://img.shields.io/badge/Citations-1-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|FACCT <br>2022|Measuring the Carbon Intensity of AI in Cloud Instances|AI2| [[paper]](https://dl.acm.org/doi/pdf/10.1145/3531146.3533234)![Scholar citations](https://img.shields.io/badge/Citations-1-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|Arxiv <br>2023|GreenScale: Carbon-Aware Systems for Edge Computing|KU| [[paper]](https://Arxiv.org/pdf/2304.00404.pdf)![Scholar citations](https://img.shields.io/badge/Citations-1-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|MLSys <br>2022|Sustainable AI: Environmental Implications, Challenges and Opportunities|Meta | [[paper]](https://proceedings.mlsys.org/paper_files/paper/2022/file/462211f67c7d858f663355eff93b745e-Paper.pdf)![Scholar citations](https://img.shields.io/badge/Citations-1-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|HotCarbon <br>2023|Peeling Back the Carbon Curtain: Carbon Optimization Challenges in Cloud Computing|CMU| [[paper]](https://hotcarbon.org/2023/pdf/a8-wang.pdf)![Scholar citations](https://img.shields.io/badge/Citations-1-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|Arxiv <br>2023|Is TinyML Sustainable?Assessing the Environmental Impacts of Machine Learning on Microcontrollers|Harvard| [[paper]](https://Arxiv.org/pdf/2301.11899.pdf)![Scholar citations](https://img.shields.io/badge/Citations-1-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|JCP <br>2021|Assessing the embodied carbon footprint of IoT edge devices with a bottom-up life-cycle approach|UCLouvain| [[paper]](https://Arxiv.org/abs/2105.02082)![Scholar citations](https://img.shields.io/badge/Citations-1-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|ICAIS <br>2023|Carbon Neutrality Approaches for IoT-Enabled Applications|IIIKT| [[paper]](https://ieeexplore.ieee.org/document/10073921)![Scholar citations](https://img.shields.io/badge/Citations-1-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|ECEE <br>2023|Sustainability of Machine Learning Models: An Energy Consumption Centric Evaluation|LBU| [[paper]](https://ieeexplore.ieee.org/document/10101532)![Scholar citations](https://img.shields.io/badge/Citations-1-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|Arxiv <br>2023|XGen-7B Technical Report|SFR| [[paper]](https://Arxiv.org/pdf/2309.03450.pdf)![Scholar citations](https://img.shields.io/badge/Citations-1-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|ERC <br>2023|How to estimate carbon footprint when training deep learning models? A guide and review|Cité U| [[paper]](https://iopscience.iop.org/article/10.1088/2515-7620/acf81b/pdf)![Scholar citations](https://img.shields.io/badge/Citations-1-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|Arxiv <br>2021|Carbon Emissions and Large Neural Network Training|UCB| [[paper]](https://Arxiv.org/pdf/2104.10350)![Scholar citations](https://img.shields.io/badge/Citations-1-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|IJEEE <br>2022|Capping carbon emission from green data centers|UAuburn| [[paper]](https://link.springer.com/article/10.1007/s40095-022-00539-9)![Scholar citations](https://img.shields.io/badge/Citations-1-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|SEGN <br>2020|The global energy footprint of information and communication technology electronics in connected Internet-of-Things devices|ORNL| [[paper]](sciencedirect.com/science/article/pii/S2352467720303398#sec4)![Scholar citations](https://img.shields.io/badge/Citations-1-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|Hotcarbon <br>2023|Carbon-Aware Memory Placement|UPotsdam| [[paper]](https://dl.acm.org/doi/abs/10.1145/3604930.3605714)![Scholar citations](https://img.shields.io/badge/Citations-1-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|TPS <br>2021|Carbon-Aware Computing for Datacenters|Google| [[paper]](https://ieeexplore.ieee.org/document/9770383?denied=)![Scholar citations](https://img.shields.io/badge/Citations-1-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|Arxiv <br>2023|Sustainable HPC: Modeling, Characterization, and Implications of Carbon Footprint in Modern HPC Systems|Northeastern University| [[paper]](https://Arxiv.org/abs/2306.13177)![Scholar citations](https://img.shields.io/badge/Citations-1-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|GLOBECOM <br>2022|Carbon-Neutralized Task Scheduling for Green Computing Networks|MediaTek | [[paper]](https://Arxiv.org/abs/2209.02198)![Scholar citations](https://img.shields.io/badge/Citations-1-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|RSER <br>2023|Assessing embodied carbon emissions of communication user devices by combining approaches|Ericsson Research| [[paper]](https://www.sciencedirect.com/science/article/pii/S1364032123002794)![Scholar citations](https://img.shields.io/badge/Citations-1-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|HotCarbon <br>2023|Towards Application Centric Carbon Emission Management|RU| [[paper]](https://dl.acm.org/doi/abs/10.1145/3604930.3605725)![Scholar citations](https://img.shields.io/badge/Citations-1-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|HotCarbon <br>2023|carbond: An Operating-System Daemon for Carbon Awareness|SIC| [[paper]](https://dl.acm.org/doi/abs/10.1145/3604930.3605707)![Scholar citations](https://img.shields.io/badge/Citations-1-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|HotCarbon <br>2023|Bringing Carbon Awareness to Multi-cloud Application Delivery|UMA| [[paper]](https://hotcarbon.org/2023/pdf/a6-maji.pdf)![Scholar citations](https://img.shields.io/badge/Citations-1-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|HotCarbon <br>2024|Myths and Misconceptions Around Reducing Carbon Embedded in Cloud Platforms|UToronto| [[paper]](https://hotcarbon.org/2023/pdf/a7-lyu.pdf)![Scholar citations](https://img.shields.io/badge/Citations-1-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|HotCarbon <br>2023|Towards Carbon Footprint Management in Hybrid Multicloud|IBM| [[paper]](https://hotcarbon.org/2023/pdf/a9-arora.pdf)![Scholar citations](https://img.shields.io/badge/Citations-1-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|HotCarbon <br>2023|An Agile Pathway Towards Carbon-aware Clouds|UW| [[paper]](https://hotcarbon.org/2023/pdf/a10-patel.pdf)![Scholar citations](https://img.shields.io/badge/Citations-1-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|HotCarbon <br>2022|Metrics for Sustainability in Data Centers|SBU| [[paper]](https://hotcarbon.org/2022/pdf/hotcarbon22-gandhi.pdf)![Scholar citations](https://img.shields.io/badge/Citations-1-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|HotCarbon <br>2023|Towards a Methodology and Framework for AI Sustainability Metrics|IBM| [[paper]](https://hotcarbon.org/2023/pdf/a13-eilam.pdf)![Scholar citations](https://img.shields.io/badge/Citations-1-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|HotCarbon <br>2023|Toward a Life Cycle Assessment for the Carbon Footprint of Data|UChicago| [[paper]](https://hotcarbon.org/2023/pdf/a14-mersy.pdf)![Scholar citations](https://img.shields.io/badge/Citations-1-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|HotCarbon <br>2023|Carbon-Efficient Neural Architecture Search|WPI| [[paper]](https://hotcarbon.org/2023/pdf/a12-zhao.pdf)![Scholar citations](https://img.shields.io/badge/Citations-1-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|HotCarbon <br>2023|Reducing the Carbon Impact of Generative AI Inference (today and in 2035)|UChicago| [[paper]](https://hotcarbon.org/2023/pdf/a11-chien.pdf)![Scholar citations](https://img.shields.io/badge/Citations-1-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|HotCarbon <br>2023|Carbon-Efficient Design Optimization for Computing Systems|Harvard| [[paper]](https://hotcarbon.org/2023/pdf/a16-elgamal.pdf)![Scholar citations](https://img.shields.io/badge/Citations-1-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|JNCA <br>2022|Recent advances in energy management for Green-IoT: An up-to-date and comprehensive survey|USorbonne| [[paper]](https://www.sciencedirect.com/science/article/pii/S1084804521002551)![Scholar citations](https://img.shields.io/badge/Citations-1-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|IEEE Networking Letters <br>2023|Less Carbon Footprint in Edge Computing by Joint Task Offloading and Energy Sharing|UUMS| [[paper]](https://ieeexplore.ieee.org/abstract/document/10154013)![Scholar citations](https://img.shields.io/badge/Citations-1-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|IMCOM <br>2023|Lightweight energy-efficient offloading framework for mobile edge/cloud computing|NU| [[paper]](https://ieeexplore.ieee.org/abstract/document/10035628)![Scholar citations](https://img.shields.io/badge/Citations-1-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|ICICC <br>2022|Shifting from Cloud Computing to Green Cloud and Edge Computing|NHU| [[paper]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4387781)![Scholar citations](https://img.shields.io/badge/Citations-1-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|HotCarbon <br>2023|On the Promise and Pitfalls of Optimizing Embodied Carbon|UMASS| [[paper]](https://dl.acm.org/doi/abs/10.1145/3604930.3605710)![Scholar citations](https://img.shields.io/badge/Citations-1-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|MICCAI <br>2022|Carbon Footprint of Selecting and Training Deep Learning Models for Medical Image Analysis|UCPH| [[paper]](https://Arxiv.org/pdf/2203.02202.pdf)![Scholar citations](https://img.shields.io/badge/Citations-1-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|HotCarbon <br>2023|EnergAt: Fine-Grained Energy Attribution for Multi-Tenancy|ETH| [[paper]](https://Arxiv.org/abs/2307.05647)![Scholar citations](https://img.shields.io/badge/Citations-1-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|HotCarbon <br>2022|Carbon Dependencies in Datacenter Design and Management|Meta| [[paper]](https://hotcarbon.org/2022/pdf/hotcarbon22-acun.pdf)![Scholar citations](https://img.shields.io/badge/Citations-1-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|Arxiv <br>2021|Towards a systematic survey for carbon neutral data centers.|NTU| [[paper]](https://Arxiv.org/abs/2110.09284)![Scholar citations](https://img.shields.io/badge/Citations-1-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|HotCarbon <br>2022|Beyond PUE: Flexible Datacenters Empowering the Cloud to Decarbonize|UChicago| [[paper]](https://hotcarbon.org/2022/pdf/hotcarbon22-chien.pdf)![Scholar citations](https://img.shields.io/badge/Citations-1-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|HotCarbon <br>2022|Multiple smaller base stations are greener than a single powerful one: Densification of Wireless Cellular Networks|UCSD| [[paper]](https://hotcarbon.org/2022/pdf/hotcarbon22-gupta.pdf)![Scholar citations](https://img.shields.io/badge/Citations-1-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|HotCarbon <br>2022|Toward Carbon-Aware Networking|Ox| [[paper]](https://hotcarbon.org/2022/pdf/hotcarbon22-zilberman.pdf)![Scholar citations](https://img.shields.io/badge/Citations-1-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|HotCarbon <br>2022|The Dirty Secret of SSDs: Embodied Carbon|UWM| [[paper]](https://Arxiv.org/abs/2207.10793)![Scholar citations](https://img.shields.io/badge/Citations-1-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|ICACT <br>2019|PUE or GPUE: A Carbon-Aware Metric for Data Centers|KAIST| [[paper]](https://ieeexplore.ieee.org/document/8701895)![Scholar citations](https://img.shields.io/badge/Citations-1-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|RCR <br>2022|Life cycle assessment of emerging technologies on value recovery from hard disk drives.|UA| [[paper]](https://www.sciencedirect.com/science/article/pii/S0921344920301026)![Scholar citations](https://img.shields.io/badge/Citations-1-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
## Contribute

We welcome contributions to [this repository](https://github.com/zhaoyujieseberena/Carbon). To add new papers to this list, please update csv files under `./res/papers.csv`. Our bots will update the paper list in `README.md` automatically. The citations of newly added papers will be updated within one day.
