---
#
# You don't need to edit this file, it's empty on purpose.
# Edit sleeks's default layout instead if you wanna make some changes
# See: https://jekyllrb.com/docs/themes/#overriding-theme-defaults
#
layout: page
title: 컴퓨터이론 및 응용 연구실
secondtitle: Computer Theory and Applications Lab
---

<div style="background: #fff6ff; padding: 3px; border: 3px solid lightgray; margin: 2px; width:70%; text-align: center; margin-left: auto; margin-right:auto;" markdown=1>
&nbsp;목&nbsp;&nbsp;&nbsp;&nbsp;표&nbsp;
{: style="font-size: 170%; text-align: center; font-weight: 600; text-underline-offset:6px; text-decoration:underline;"}

이론이 실제를 만나는 곳을 추구한다  
We pursue where theory meets practice  
{: style="font-size: 130%; text-align: center; font-weight: 600;"}


<div style="text-align:center">
<table cellspacing="0" cellpadding="0" class='center'>
<td>세계 최고의 연구</td>
<td>현실에 응용되는 연구</td>
</table>
</div>
</div>

<br/>

<style>
table, table tr, table td {
    border: none;
    font-size: 105%;
    font-weight: 600;
    width : 66%;
  margin-left: auto;
  margin-right: auto;
}
table td { width : 50%;​}
</style>


컴퓨터이론은 컴퓨터공학의 기초학문으로서 효율적인 알고리즘 개발, NP-complete 개념, 현대 암호학 이론 등으로 컴퓨터공학 발전에 근본적인 기여를 하여 왔다. Turing Award를 받은 다수의 컴퓨터이론 학자들이 이러한 사실을 잘 보여주고 있다. 

본 연구실은 컴퓨터이론 및 응용에 대해 연구하는 곳으로 구체적으로 그래프 알고리즘, 스트링 알고리즘, 암호학, bioinformatics, 금융공학 등에 대해 연구하고 있다.

빅데이터는 대부분 스트링 데이터(text, bio-sequence 등)이거나 그래프 데이터(social network, bio-network, web graph 등)로 존재한다. 최근에는 스트링 및 그래프 형태의 빅데이터를 빠르게 분석하는 알고리즘에 대해 활발하게 연구하고 있다.

## Research Area
<div class="container">
    <div class="post-list" itemscope="" itemtype="http://schema.org/Blog">
    {% assign areas = site.areas %} 
    {% assign sorted_areas = areas | sort: "importance" %} 
    {% for area in sorted_areas %}
    {% include areacard.html %}
    {% endfor %}
    <!-- {% include pagination.html %} -->
    </div>
</div>

<style>
    table th {
        font-size:1.1rem;
        font-weight:bold;
        border: 0px;
        padding : 0px;
        width: 10%;
        background-color : #ffffff;
    }
    thead {
        border: 0px;
    }
    .summary {
      font-size: 1rem;
      font-weight: normal;
    }
</style>


<div class="news">
  <a href="/news"><h2>Recent News</h2></a>
  {% if site.news  %}
    <div class="table-responsive">
      <table class="table table-sm table-borderless">
      {% assign news = site.news | where: "on-home", "true" | reverse %}
      {% for item in news limit: site.news_limit %}
        <tr>
          <th scope="row">{{ item.date | date: "%b %-d, %Y" }}</th>
          <td>
            {% if item.inline %}
              {{ item.content | remove: '<p>' | remove: '</p>' | emojify }}
            {% else %}
              <a class="news-title" href="{{ item.permalink | relative_url }}">{{ item.title | remove: '<p>' | remove: '</p>' | replace: '<br/>', " " }}</a><br/>
              <div class="summary">
              {{ item.content | remove: '<p>' | remove: '</p>' | emojify | truncatewords:50 }}
              </div>
            {% endif %}
          </td>
        </tr>
      {% endfor %}
      </table>
    </div>
  {% else %}
    <p>No news so far...</p>
  {% endif %}
</div>