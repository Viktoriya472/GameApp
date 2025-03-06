<h3 tabindex="-1" class="heading-element" dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
Сайт посвящён компьютерным играм и игровой индустрии. 
<br>Раздел «Новости» содержит околоигровые и киберспортивные новости.
<br>На форуме обсуждаются конкретные игры и все, что с ними связано.
</font></font></h3>
<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Установка</font></font></h2><a id="user-content-installation" class="anchor" aria-label="Постоянная ссылка: Установка" href="#installation"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"></svg></a></div>
<ul>
  <li>
    <strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Шаг 1</font></font></strong>
    <font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> : Клонируйте исходный код с GitHub</font></font>
  </li>
  <div class="snippet-clipboard-content notranslate position-relative overflow-auto"><pre class="notranslate"><code>git clone https://github.com/Viktoriya472/GameApp.git
 </code></pre>
    <div class="zeroclipboard-container">
      <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="git clone https://github.com/Viktoriya472/GameApp.git
        " tabindex="0" role="button">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon"></svg>
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none"></svg>
      </clipboard-copy>
    </div>
  </div>
  <li><strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Шаг 2</font></font></strong>
    <font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> : Создайте и используйте виртуальную среду (python 3.11) с помощью </font></font><code>venv</code>
  </li>
  <div class="snippet-clipboard-content notranslate position-relative overflow-auto"><pre class="notranslate"><code>python -m venv .venv
.venv/scripts/activate</code></pre>
    <div class="zeroclipboard-container">
      <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="python -m venv .venv
.venv/scripts/activate" tabindex="0" role="button">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon"></svg>
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none"></svg>
      </clipboard-copy>
    </div>
  </div>
  <li>
    <strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Шаг 3</font></font></strong>
    <font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> : Установите зависимости проекта</font></font>
  </li>
<div class="snippet-clipboard-content notranslate position-relative overflow-auto"><pre class="notranslate"><code>cd .\GameApp\
pip install -r requirements.txt</code></pre>
    <div class="zeroclipboard-container">
      <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="cd .\GameApp\
pip install -r requirements.txt" tabindex="0" role="button">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon"></svg>
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none"></svg>
      </clipboard-copy>
    </div>
  </div>
  <li>
  <strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Шаг 4</font></font></strong>
  <font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> : Запустите сервер</font></font>
  </li>
    <div class="snippet-clipboard-content notranslate position-relative overflow-auto"><pre class="notranslate"><code>python manage.py runserver
 </code></pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="jmilkfansblog-manager server" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon"></svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none"></svg>
    </clipboard-copy>
  </div></div>
</ul>
<h2 tabindex="-1" class="heading-element" dir="auto"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Асинхронная рассылка с Celery</font></font></h2>
<ul>
  <li>
  <strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Шаг 1</font></font></strong>
  <font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> : Установите Redis в качестве брокера Celery и серверной части базы данных</font></font>
  </li>
  <div class="snippet-clipboard-content notranslate position-relative overflow-auto"><pre class="notranslate"><code>docker pull redis:latest
docker run --name redis-server -p 6379:6379 -d redis:latest</code></pre>
    <div class="zeroclipboard-container">
      <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="docker pull redis:latest
docker run --name redis-server -p 6379:6379 -d redis:latest" tabindex="0" role="button">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon"></svg>
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none"></svg>
      </clipboard-copy>
    </div>
  </div>
  <li><strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Шаг 2</font></font></strong>
    <font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> : Запустите Celery в качестве очереди задач (в новом терминале)</font></font>
  </li>
  <div class="snippet-clipboard-content notranslate position-relative overflow-auto"><pre class="notranslate"><code>celery -A gameApp worker -l info -P eventlet
</code></pre>
    <div class="zeroclipboard-container">
      <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="celery -A gameApp worker -l info -P eventlet
        " tabindex="0" role="button">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon"></svg>
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none"></svg>
      </clipboard-copy>
    </div>
  </div>
  <li><strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Шаг 3</font></font></strong>
    <font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> : Запустите Celery beat для планирования периодических задач (в новом терминале)</font></font>
  </li>
  <div class="snippet-clipboard-content notranslate position-relative overflow-auto"><pre class="notranslate"><code>celery -A gameApp beat -l info
 </code></pre>
    <div class="zeroclipboard-container">
      <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="celery -A gameApp beat -l info
        " tabindex="0" role="button">
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon"></svg>
        <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none"></svg>
      </clipboard-copy>
    </div>
  </div>
  
</ul>
