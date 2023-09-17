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

## Exisiting metrics
| Metric    | Paper Title                                                                             | Description                                                     | Included carbon life cycle stage(s) |
| --------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------- | ----------------------------------- |
| PUE       | PUE™: A Comprehensive Examination of the Metric.                                        | the Power Usage Effectiveness (PUE) of a dedicated data center, | Operation                           |
| GPUE      | PUE or GPUE: A carbon-aware metric for data centers.                                    | Green Power Usage Effectiveness                                 | Operation                           |
| CUE       | Carbon Usage Effectiveness (CUE): A Green Grid Data Center Sustainability Metric.       | Carbon Usage Effectiveness                                      | Operation                           |
| CCI       | Junkyard computing: repurposing discarded smartphones to minimize carbon                | Computational Carbon Intensity                                  | Operation                           |
| SCI       | Software Carbon Intensity Standard. Version 1.0.0. (Nov. 1, 2021).                      | Software Carbon Intensity                                       | Operation, Manufacturing            |
| CDP/CEP   | ACT: Designing Sustainable Computer Systems With An Architectural Carbon Modeling Tool  | Carbon Delay/Energy Product                                     | Operation, Manufacturing            |
| tCDP/tCEP | Design Space Exploration and Optimization for Carbon-Efficient Extended Reality Systems | the product of total CO2𝑒 and total application execution time  | Operation, Manufacturing            |
| JSC       | Metrics for Sustainability in Data Centers                                              | Job Sustainability Costs                                        | Operation, Manufacturing            |
| ASC       | Metrics for Sustainability in Data Centers                                              | Amortized Sustainability Costs                                  | Operation, Manufacturing            |
## Useful Links
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
### Review
| Venue | Year | Title | Affiliation | &nbsp;&nbsp;&nbsp;&nbsp;Link&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 
| :---: | :---: | :----: | :---------: | :---: |
|ICAIS|2023|Carbon Neutrality Approaches for IoT-Enabled Applications|IIIKT| [[paper]](https://ieeexplore.ieee.org/document/10073921)![Scholar citations](https://img.shields.io/badge/Citations-0-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|ERC|2023|How to estimate carbon footprint when training deep learning models? A guide and review|Cité U| [[paper]](https://iopscience.iop.org/article/10.1088/2515-7620/acf81b/pdf)![Scholar citations](https://img.shields.io/badge/Citations-0-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|HotCarbon|2024|Myths and Misconceptions Around Reducing Carbon Embedded in Cloud Platforms|UToronto| [[paper]](https://hotcarbon.org/2023/pdf/a7-lyu.pdf)![Scholar citations](https://img.shields.io/badge/Citations-0-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|HotCarbon|2023|Towards Carbon Footprint Management in Hybrid Multicloud|IBM| [[paper]](https://hotcarbon.org/2023/pdf/a9-arora.pdf)![Scholar citations](https://img.shields.io/badge/Citations-0-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|HotCarbon|2023|An Agile Pathway Towards Carbon-aware Clouds|UW| [[paper]](https://hotcarbon.org/2023/pdf/a10-patel.pdf)![Scholar citations](https://img.shields.io/badge/Citations-0-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|HotCarbon|2023|Reducing the Carbon Impact of Generative AI Inference (today and in 2035)|UChicago| [[paper]](https://hotcarbon.org/2023/pdf/a11-chien.pdf)![Scholar citations](https://img.shields.io/badge/Citations-0-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|JNCA|2022|Recent advances in energy management for Green-IoT: An up-to-date and comprehensive survey|USorbonne| [[paper]](https://www.sciencedirect.com/science/article/pii/S1084804521002551)![Scholar citations](https://img.shields.io/badge/Citations-42-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|Arxiv|2021|Towards a systematic survey for carbon neutral data centers.|NTU| [[paper]](https://Arxiv.org/abs/2110.09284)![Scholar citations](https://img.shields.io/badge/Citations-21-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|HotCarbon|2022|Toward Carbon-Aware Networking|Ox| [[paper]](https://hotcarbon.org/2022/pdf/hotcarbon22-zilberman.pdf)![Scholar citations](https://img.shields.io/badge/Citations-2-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|
### Optimation
| Venue | Year | Title | Affiliation | &nbsp;&nbsp;&nbsp;&nbsp;Link&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 
| :---: | :---: | :----: | :---------: | :---: |
|TCADICS |2022|ESSENCE: Exploiting Structured Stochastic Gradient Pruning for Endurance-Aware ReRAM-Based In-Memory Training Systems|Duke| [[paper]](https://ieeexplore.ieee.org/document/9926186)![Scholar citations](https://img.shields.io/badge/Citations-2-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|ICCAD|2020|ReTransformer: ReRAM-based Processing-in-Memory Architecture for Transformer Acceleration|Duke | [[paper]](https://ieeexplore.ieee.org/document/9256523)![Scholar citations](https://img.shields.io/badge/Citations-38-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|ASPLOS|2023|Carbon Explorer: A Holistic Framework for Designing Carbon Aware Datacenters|Meta| [[paper]](https://Arxiv.org/pdf/2201.10036.pdf)![Scholar citations](https://img.shields.io/badge/Citations-24-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|Arxiv|2023|Towards Sustainable Computing: Accessing the Cabon Footprint of Heterogeneous Systems|ASU| [[paper]](https://Arxiv.org/abs/2306.09434)![Scholar citations](https://img.shields.io/badge/Citations-0-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|Micro|2022|Sustainable AI Processing at the Edge|PITT| [[paper]](https://Arxiv.org/pdf/2207.01209.pdf)![Scholar citations](https://img.shields.io/badge/Citations-2-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|Arxiv|2023|When the Metaverse Meets Carbon Neutrality: Ongoing Efforts and Directions|HUST| [[paper]](https://Arxiv.org/pdf/2301.10235.pdf)![Scholar citations](https://img.shields.io/badge/Citations-4-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|FACCT|2022|Measuring the Carbon Intensity of AI in Cloud Instances|AI2| [[paper]](https://dl.acm.org/doi/pdf/10.1145/3531146.3533234)![Scholar citations](https://img.shields.io/badge/Citations-51-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|Arxiv|2023|GreenScale: Carbon-Aware Systems for Edge Computing|KU| [[paper]](https://Arxiv.org/pdf/2304.00404.pdf)![Scholar citations](https://img.shields.io/badge/Citations-0-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|MLSys|2022|Sustainable AI: Environmental Implications, Challenges and Opportunities|Meta | [[paper]](https://proceedings.mlsys.org/paper_files/paper/2022/file/462211f67c7d858f663355eff93b745e-Paper.pdf)![Scholar citations](https://img.shields.io/badge/Citations-127-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|HotCarbon|2023|Peeling Back the Carbon Curtain: Carbon Optimization Challenges in Cloud Computing|CMU| [[paper]](https://hotcarbon.org/2023/pdf/a8-wang.pdf)![Scholar citations](https://img.shields.io/badge/Citations-0-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|ICAIS|2023|Carbon Neutrality Approaches for IoT-Enabled Applications|IIIKT| [[paper]](https://ieeexplore.ieee.org/document/10073921)![Scholar citations](https://img.shields.io/badge/Citations-0-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|Hotcarbon|2023|Carbon-Aware Memory Placement|UPotsdam| [[paper]](https://dl.acm.org/doi/abs/10.1145/3604930.3605714)![Scholar citations](https://img.shields.io/badge/Citations-0-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|GLOBECOM|2022|Carbon-Neutralized Task Scheduling for Green Computing Networks|MediaTek | [[paper]](https://Arxiv.org/abs/2209.02198)![Scholar citations](https://img.shields.io/badge/Citations-3-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|HotCarbon|2023|Towards Application Centric Carbon Emission Management|RU| [[paper]](https://dl.acm.org/doi/abs/10.1145/3604930.3605725)![Scholar citations](https://img.shields.io/badge/Citations-0-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|HotCarbon|2023|carbond: An Operating-System Daemon for Carbon Awareness|SIC| [[paper]](https://dl.acm.org/doi/abs/10.1145/3604930.3605707)![Scholar citations](https://img.shields.io/badge/Citations-0-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|HotCarbon|2023|Carbon-Efficient Neural Architecture Search|WPI| [[paper]](https://hotcarbon.org/2023/pdf/a12-zhao.pdf)![Scholar citations](https://img.shields.io/badge/Citations-0-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|HotCarbon|2023|Carbon-Efficient Design Optimization for Computing Systems|Harvard| [[paper]](https://hotcarbon.org/2023/pdf/a16-elgamal.pdf)![Scholar citations](https://img.shields.io/badge/Citations-0-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|IEEE Networking Letters|2023|Less Carbon Footprint in Edge Computing by Joint Task Offloading and Energy Sharing|UUMS| [[paper]](https://ieeexplore.ieee.org/abstract/document/10154013)![Scholar citations](https://img.shields.io/badge/Citations-1-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|IMCOM|2023|Lightweight energy-efficient offloading framework for mobile edge/cloud computing|NU| [[paper]](https://ieeexplore.ieee.org/abstract/document/10035628)![Scholar citations](https://img.shields.io/badge/Citations-0-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|ICICC|2022|Shifting from Cloud Computing to Green Cloud and Edge Computing|NHU| [[paper]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4387781)![Scholar citations](https://img.shields.io/badge/Citations-1-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|HotCarbon|2023|On the Promise and Pitfalls of Optimizing Embodied Carbon|UMASS| [[paper]](https://dl.acm.org/doi/abs/10.1145/3604930.3605710)![Scholar citations](https://img.shields.io/badge/Citations-1-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|HotCarbon|2023|EnergAt: Fine-Grained Energy Attribution for Multi-Tenancy|ETH| [[paper]](https://Arxiv.org/abs/2307.05647)![Scholar citations](https://img.shields.io/badge/Citations-0-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|HotCarbon|2022|Carbon Dependencies in Datacenter Design and Management|Meta| [[paper]](https://hotcarbon.org/2022/pdf/hotcarbon22-acun.pdf)![Scholar citations](https://img.shields.io/badge/Citations-2-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|HotCarbon|2022|Multiple smaller base stations are greener than a single powerful one: Densification of Wireless Cellular Networks|UCSD| [[paper]](https://hotcarbon.org/2022/pdf/hotcarbon22-gupta.pdf)![Scholar citations](https://img.shields.io/badge/Citations-1-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|
### Calculation
| Venue | Year | Title | Affiliation | &nbsp;&nbsp;&nbsp;&nbsp;Link&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 
| :---: | :---: | :----: | :---------: | :---: |
|
### Standardization
| Venue | Year | Title | Affiliation | &nbsp;&nbsp;&nbsp;&nbsp;Link&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 
| :---: | :---: | :----: | :---------: | :---: |
|ISCA|2022|ACT: Designing sustainable computer systems with an architectural carbon modeling tool|Harvard| [[paper]](https://ieeexplore.ieee.org/document/10122998)![Scholar citations](https://img.shields.io/badge/Citations-37-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|Arxiv|2023|Design space exploration and optimization for carbon-efficient extended reality systems|Harvard | [[paper]](https://Arxiv.org/abs/2305.01831)![Scholar citations](https://img.shields.io/badge/Citations-2-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|IJEEE|2022|Capping carbon emission from green data centers|UAuburn| [[paper]](https://link.springer.com/article/10.1007/s40095-022-00539-9)![Scholar citations](https://img.shields.io/badge/Citations-3-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|HotCarbon|2023|Towards Application Centric Carbon Emission Management|RU| [[paper]](https://dl.acm.org/doi/abs/10.1145/3604930.3605725)![Scholar citations](https://img.shields.io/badge/Citations-0-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|HotCarbon|2023|Bringing Carbon Awareness to Multi-cloud Application Delivery|UMA| [[paper]](https://hotcarbon.org/2023/pdf/a6-maji.pdf)![Scholar citations](https://img.shields.io/badge/Citations-0-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|HotCarbon|2022|Metrics for Sustainability in Data Centers|SBU| [[paper]](https://hotcarbon.org/2022/pdf/hotcarbon22-gandhi.pdf)![Scholar citations](https://img.shields.io/badge/Citations-6-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|HotCarbon|2023|Towards a Methodology and Framework for AI Sustainability Metrics|IBM| [[paper]](https://hotcarbon.org/2023/pdf/a13-eilam.pdf)![Scholar citations](https://img.shields.io/badge/Citations-0-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|HotCarbon|2023|Toward a Life Cycle Assessment for the Carbon Footprint of Data|UChicago| [[paper]](https://hotcarbon.org/2023/pdf/a14-mersy.pdf)![Scholar citations](https://img.shields.io/badge/Citations-0-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|HotCarbon|2022|Beyond PUE: Flexible Datacenters Empowering the Cloud to Decarbonize|UChicago| [[paper]](https://hotcarbon.org/2022/pdf/hotcarbon22-chien.pdf)![Scholar citations](https://img.shields.io/badge/Citations-6-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
|ICACT|2019|PUE or GPUE: A Carbon-Aware Metric for Data Centers|KAIST| [[paper]](https://ieeexplore.ieee.org/document/8701895)![Scholar citations](https://img.shields.io/badge/Citations-4-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)|
## Contribute

We welcome contributions to [this repository](https://github.com/zhaoyujieseberena/Carbon). To add new papers to this list, please update csv files under `./res/papers.csv`. Our bots will update the paper list in `README.md` automatically. The citations of newly added papers will be updated within one day.
