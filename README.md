# Px To Em

1. Select a value in px form or em
2. Use hot key to toggle between the formats<br />
<code>16px <----> 1rem </code><br />
<code>18px <----> 1.125rem </code><br /><br /><br />


# Installation
1. Open Sublime and choose <code>preferences->browse packages</code>
2. Make a new plugin folder called PxToEm and clone this repo there.

# Usage
1. Select text to convert ie. <code>16px 20em</code>
2. use Shortcut <code>ctrl+shift+E+up</code>
OR Right click menu option available. <code>Right Click</code> and click <code>Convert PX <--> EM</code>

# Settings
1. To access settings navigate to <code>preferences->package settings->PxToEM->Package Settings - default</code>
2. Settings can all be viewed in the location above at pxtoem/sublime_package/settings.sublime-settings
<ul>
<li><code>basePixel</code> -<i>int</i>- the base pixel used for the current project, in most cases the browser is 16. The default setting is 16.</li>
<li><code>useRem</code> -<i>boolean</i>- this will return conversions with the 'rem' appendage in replace of 'em'. This is turned off by default.</li>
</ul> 
