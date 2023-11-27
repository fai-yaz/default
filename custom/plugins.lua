local plugins = {
  {
    "lervag/vimtex",
    lazy = false,
    config = function()
      require "custom.configs.vimtex"
    end
  },
  {
    "iamcco/markdown-preview.nvim",
    cmd = { "MarkdownPreviewToggle", "MarkdownPreview", "MarkdownPreviewStop" },
    ft = { "markdown" },
    build = function() vim.fn["mkdp#util#install"]() end,
  },
  -- In order to modify the `lspconfig` configuration:
  {
    "neovim/nvim-lspconfig",
    config = function()
      require "plugins.configs.lspconfig"
      require "custom.configs.lspconfig"
    end,
  },
  {
    "williamboman/mason.nvim",
    opts = {
      ensure_installed ={
        "prettier",
        "lua-language-server",
        "html-lsp",
        "marksman"
      }
    }
  }
}
return plugins
