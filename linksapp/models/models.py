# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ErpLinkler(models.Model):
     _name = 'erpuygulamalar.linkler'

     name = fields.Char(string="Baslik", required=True)
     linkname = fields.Text(string="Link", required=True)
     linkurl = fields.Char(string="Url", compute='_url_olustur')
     description = fields.Text(string="Aciklama")
     logo = fields.Binary(string="Logo", attachment=True)
     kisaltma = fields.Char(string="Kısaltma")
     isapp = fields.Boolean('App mi?', default=False)
     # active = fields.Boolean('Active', default=True)

     kategori_id = fields.Many2one('erpuygulamalar.kategori',ondelete='set null', string="Kategori", required=True)
     kategori_name = fields.Char('Kategori İsmi', related='kategori_id.name', readonly=True)
     kategori_description = fields.Text('Kategori Açıklaması', related='kategori_id.description', readonly=False)


     @api.depends('linkname', 'name')
     def _url_olustur(self):
          for r in self:
               if not r.linkname:
                    r.linkurl = "#"
               else:
                    r.linkurl = "<a href='"+r.linkname+"' target='_blank'>"+r.name+"</a>"


class Kategori(models.Model):
     _name = 'erpuygulamalar.kategori'
     _rec_name = 'strbirlestir'


     name = fields.Char(string="Kategori", required=True)
     description = fields.Text(string="Kategori Açıklaması")

     link_ids = fields.One2many('erpuygulamalar.linkler','kategori_id', string="Uygulamalar")
     strbirlestir = fields.Char(string="Birlekştirilen", compute='_str_birlestir')
     link_count = fields.Integer(string="Uygulama Sayısı", compute='_get_links_count', store=True)
     measure_test = fields.Integer(string="sabit", compute='_sabit_deger_ata')
      # link_count_odooApp = fields.Integer(string="Odoo Uygulama Sayısı", compute='find_applinks', store=True)
     # isapp false olanları al

     @api.depends('name', 'description')
     def _str_birlestir(self):
          for r in self:
               if not r.description:
                    r.strbirlestir = r.name
               else:
                    r.strbirlestir = r.name + " - " + r.description\

     @api.depends('link_ids')
     def _get_links_count(self):
               self.link_count = len(self.link_ids)

                # self.link_count = self.link_ids.search(
                #     [('isapp', '=', True)])
               # domain = [('isapp', '=', 'True')]
               # self.link_count = len(self.link_ids.search(domain))
               # partners = self.env['res.partner'].search(domain)

     # def _sabit_deger_ata(self):
     #      self.measure_test = 15
     #
     # @api.multi
     # def find_applinks(self):
     #      PartnerObj = self.env['erpuygulamalar.linkler']
     #      domain = [
     #           ('isapp', '=', 'True')
     #      ]
     #      self.link_count_odooApp = len(PartnerObj.search(domain))