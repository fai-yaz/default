local wezterm = require 'wezterm'

local module = {}
local keys = {}
local mux = wezterm.mux

local function error_logger()
	wezterm.log_error 'test error logged'
end

function module.apply_to_config(config)
	error_logger()

	
	config.color_scheme = 'AdventureTime'
	config.font = wezterm.font 'JetBrains Mono'

	enable_tab_bar = false
	hide_tab_bar_if_only_one_tab = true

	-- true is default, false is retro 
	use_fancy_tab_bar = false


	-- styling inactive panes
	config.inactive_pane_hsb = {
		saturation = 0.9,
		brightness = 0.8,
	}

	-- opacity
	config.window_background_opacity = 0.65
	-- background
	config.window_background_image = '/Users/faiyaz/.config/wezterm/backgrounds/spacegeyser_cropped.TIFF'

	

end

function module.key_for_config(config)
	config.keys = {
	}
end

-- function module.

return module
