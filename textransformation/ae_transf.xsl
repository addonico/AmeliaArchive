<?xml version="1.0" encoding="UTF-8" ?> 
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:tei= "http://www.tei-c.org/ns/1.0">
<xsl:output method="html" indent="yes"/>
<xsl:template match="/">
     <head>
         <meta name="viewport" content="width= device-width, initial-scale=1.0"/> 
         <title> <xsl:value-of select="/tei:TEI/tei:teiHeader/tei:fileDesc/tei:titleStmt/tei:title"/></title>
         <style>
          * { font-family: "Times New Roman";
                 }
              
              p { width: 75%;
                  text-align: justify;
                  text-justify: inter-word;
                  text-indent: 30px;
                 }
              .top { 
                     font-weight: bold;
                     text-align: center;
                     text-decoration:underline 15%;
                   }
              h3  {  
                    font-style: italic;
                    text-align: center;
                       }
              h1   {  
                       font-size: 2em;
                       font-style: bold;
                       text-align: center
                       
                       }
              h5    {  
                       font-weight: bold;
                       text-align: center;
                       }
              .article  {  
                       width: 50%;
                       float:center;
                       margin:auto;
                       position:absolute;
                       right: 25%;
                       left: 30%;
                       
                       }
               img     {  
                       float:center;
                       margin:auto;
                       
                       }
              .comment{  
                       float:center;
                       font-style: italic;
                       font-size= 1em

                       
                       }
         </style>    
     </head>
     <body>
     <div>
        <h6 class="top">The Sunday Star, Washington, D.C., September 22, 1929</h6>
        <h1><xsl:value-of select="/tei:TEI/tei:text/tei:body/tei:div[@xml:id='ttl']/tei:head[@n='3']"/></h1>
        <h3><xsl:value-of select="/tei:TEI/tei:text/tei:body/tei:div[@xml:id='ttl']/tei:head[@n='2']"/></h3>
        <h5><xsl:value-of select="/tei:TEI/tei:text/tei:body/tei:div[@xml:id='ttl']/tei:head[@n='1']"/></h5>
    </div>
    <div class="article">
        <xsl:for-each select="/tei:TEI/tei:text/tei:body/tei:div[@xml:id='content']/tei:div/tei:p">
        <p><xsl:value-of select="."/></p>
        </xsl:for-each>
        <div class="pic"><img src="" alt="placeholder"/><p class="comment"><xsl:value-of select="/tei:TEI/tei:text/tei:body/tei:div[@xml:id='container']/tei:p[@n='16']"/></p></div>
        <xsl:for-each select="/tei:TEI/tei:text/tei:body/tei:div[@xml:id='content_2']/tei:div/tei:p">
        <p><xsl:value-of select="."/></p>
        </xsl:for-each>
    </div>
    </body>
</xsl:template>
</xsl:stylesheet>
